#include <windows.h>
#include <stdio.h>

typedef struct _SERVICE {
    void (*handler)(char*);
    char name[24];
} SERVICE, *PSERVICE;

typedef struct _MSG_DATA {
    char data[32];
} MSG_DATA, *PMSG_DATA;

HANDLE hHeap;
PSERVICE global_service = NULL;

void default_handler(char* msg) {
    printf("[v] Service executing: %s\n", msg);
}

// THE "WIN" FUNCTION - Your goal is to redirect execution here.
void shell_win() {
    printf("\n[!] EXPLOIT SUCCESS: Redirected execution to shell_win!\n");
    system("cmd.exe");
}

void create_service() {
    global_service = (PSERVICE)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, sizeof(SERVICE));
    global_service->handler = default_handler;
    strcpy(global_service->name, "Legacy_Service");
    printf("[+] Service created at: %p (Handler: %p)\n", global_service, default_handler);
}

void delete_service() {
    printf("[+] Freeing Service at %p...\n", global_service);
    HeapFree(hHeap, 0, global_service);
    // VULNERABILITY: global_service is NOT set to NULL.
}

void trigger_handler() {
    if (global_service) {
        printf("[+] Attempting to call handler at %p...\n", global_service->handler);
        global_service->handler(global_service->name);
    }
}

void inject_message(char* input) {
    PMSG_DATA msg = (PMSG_DATA)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, sizeof(MSG_DATA));
    // Since MSG_DATA and SERVICE are both 32 bytes, the heap manager 
    // will likely place 'msg' exactly where 'global_service' was.
    memcpy(msg->data, input, 32);
    printf("[+] Message allocated at: %p\n", msg);
}

int main() {
    hHeap = HeapCreate(0, 0, 0); // Create a private heap for stability
    char buffer[128];
    int choice;

    printf("--- UAF Function Pointer Lab ---\n");
    printf("Target Function (shell_win) is at: %p\n", shell_win);

    while(1) {
        printf("\n1. Create  2. Delete  3. Trigger  4. Inject  5. Exit\n> ");
        if (scanf("%d", &choice) != 1) break;
        
        switch(choice) {
            case 1: create_service(); break;
            case 2: delete_service(); break;
            case 3: trigger_handler(); break;
            case 4: 
                printf("Enter 32 bytes of 'message' data: ");
                scanf("%s", buffer);
                inject_message(buffer);
                break;
            case 5: exit(0);
        }
    }
    return 0;
}