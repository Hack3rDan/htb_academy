#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct _USER_AUTH {
    void (*login_handler)(char*);
    char username[16];
} USER_AUTH, *PUSER_AUTH;

void default_login(char* name) {
    printf("[v] Logging in user: %s\n", name);
}

// THE WIN FUNCTION
void shell_win() {
    printf("\n[!] HEAP OVERFLOW SUCCESS: Redirected to shell_win!\n");
    system("cmd.exe");
}

HANDLE hHeap;
char* vul_buffer = NULL;
PUSER_AUTH victim_user = NULL;

void groom_heap() {
    // 1. Allocate the vulnerable buffer (32 bytes)
    vul_buffer = (char*)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, 32);
    
    // 2. Allocate the victim object (32 bytes on x64) immediately after
    victim_user = (PUSER_AUTH)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, sizeof(USER_AUTH));
    victim_user->login_handler = default_login;

    // These two memory blocks should be adjacent to each other in memory
    
    printf("[+] Allocated Vulnerable Buffer at: %p\n", vul_buffer);
    printf("[+] Allocated Victim User Object at: %p\n", victim_user);
    printf("[+] Current login_handler points to: %p\n", victim_user->login_handler);
}

void trigger_overflow() {
    if (!vul_buffer) return;
    
    char input[128];
    printf("\nEnter data to fill vulnerable buffer: ");
    // VULNERABILITY: No bounds checking on the input into a 32-byte buffer
    scanf("%s", input); 
    strcpy(vul_buffer, input);
    
    printf("[+] Overflow complete. Check the victim object now.\n");
}

void call_handler() {
    if (victim_user) {
        printf("[+] Executing victim_user->login_handler...\n");
        victim_user->login_handler("Guest");
    }
}

int main() {
    hHeap = HeapCreate(0, 0, 0);
    int choice;

    printf("--- Windows Heap Overflow (CWE-122) Lab ---\n");
    printf("Target Function (shell_win) is at: %p\n", shell_win);

    while(1) {
        printf("\n1. Groom Heap 2. Trigger Overflow 3. Execute Handler 4. Exit\n> ");
        if (scanf("%d", &choice) != 1) break;

        switch(choice) {
            case 1: groom_heap(); break;
            case 2: trigger_overflow(); break;
            case 3: call_handler(); break;
            case 4: exit(0);
        }
    }
    return 0;
}