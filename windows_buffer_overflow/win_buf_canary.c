#include <windows.h>
#include <stdio.h>
#include <string.h>

// THE WIN FUNCTION
void shell_win() {
    printf("\n[!] STACK BYPASS SUCCESS: Redirected to shell_win!\n");
    system("cmd.exe");
}

void vuln_function() {
    char canary_leak_buf[64];
    char overflow_buf[32];
    int choice;

    printf("--- Stack Canary Bypass Lab ---\n");
    printf("Target Function (shell_win) is at: %p\n", shell_win);

    while(1) {
        printf("\n1. Set Profile Name (Leak Source) 2. View Profile 3. Edit Bio (Overflow) 4. Exit\n> ");
        scanf("%d", &choice);
        getchar(); // clear newline

        switch(choice) {
            case 1:
                printf("Enter Profile Name: ");
                // Vulnerability: We don't null-terminate properly or allow format strings
                //fscanf(stdin,"%s",canary_leak_buf);
                fgets(canary_leak_buf, 64, stdin);
                break;

            case 2:
                printf("Profile Name: ");
                // LEAK VULNERABILITY: Printing a buffer that might contain 
                // stack data immediately following the input.
                //printf(canary_leak_buf); 
                fwrite(canary_leak_buf,64,sizeof(canary_leak_buf),stdout);
                break;

            case 3:
                printf("Enter Bio: ");
                // OVERFLOW VULNERABILITY: Reading 128 bytes into a 32-byte buffer
                gets(overflow_buf); 
                break;

            case 4:
                return;
        }
    }
}

int main() {
    vuln_function();
    return 0;
}