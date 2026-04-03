#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _USER_OBJECT {
    char name[16];
    char* bio_ptr; // This is our target for AAR/AAW
} USER_OBJECT, *PUSER_OBJECT;

HANDLE hHeap;
PUSER_OBJECT global_user = NULL;

void create_user() {
    global_user = (PUSER_OBJECT)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, sizeof(USER_OBJECT));
    global_user->bio_ptr = (char*)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, 64);
    
    strcpy(global_user->name, "TargetUser");
    strcpy(global_user->bio_ptr, "This is a default bio.");
    
    printf("[+] User created at %p\n", global_user);
    printf("[+] Bio pointer points to %p\n", global_user->bio_ptr);
}

void delete_user() {
    printf("[+] Freeing user at %p...\n", global_user);
    HeapFree(hHeap, 0, global_user);
    // VULNERABILITY: global_user is NOT set to NULL.
}

void arbitrary_read() {
    if (global_user && global_user->bio_ptr) {
        printf("\n[READ] Data at %p: %s\n", global_user->bio_ptr, global_user->bio_ptr);
    }
}

void arbitrary_write() {
    if (global_user && global_user->bio_ptr) {
        printf("\nEnter data to write to %p: ", global_user->bio_ptr);
        scanf("%24s", global_user->bio_ptr);
    }
}

void inject_payload() {
    // This allocation is the same size as USER_OBJECT (24 bytes on x64)
    // It will likely occupy the same memory block we just freed.
    char* fake_object = (char*)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, sizeof(USER_OBJECT));
    printf("\n[+] Enter 24 bytes of raw payload: ");
    
    // We use ReadFile to allow null bytes in our addresses
    DWORD bytesRead;
    ReadFile(GetStdHandle(STD_INPUT_HANDLE), fake_object, sizeof(USER_OBJECT), &bytesRead, NULL);
    
    printf("[+] Payload injected at %p\n", fake_object);
}

int main() {
    hHeap = HeapCreate(0, 0, 0);
    int choice;

    printf("--- Windows UAF AAR/AAW Lab ---\n");
    while(1) {
        printf("\n1. Create 2. Delete 3. Read 4. Write 5. Inject 6. Exit\n> ");
        if (scanf("%d", &choice) != 1) break;
        getchar(); // Clear newline

        switch(choice) {
            case 1: create_user(); break;
            case 2: delete_user(); break;
            case 3: arbitrary_read(); break;
            case 4: arbitrary_write(); break;
            case 5: inject_payload(); break;
            case 6: exit(0);
        }
    }
    return 0;
}