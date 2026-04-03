#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

HANDLE hHeap;

void lab_setup() {
    hHeap = HeapCreate(0, 0, 0); // Create a private heap
    
    // Allocate Chunk A
    char* chunkA = (char*)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, 32);
    // Allocate Chunk B (Target for metadata corruption)
    char* chunkB = (char*)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, 32);

    printf("[+] Chunk A (Vulnerable): %p\n", chunkA);
    printf("[+] Chunk B (Metadata Target): %p\n", chunkB);
    
    // In a standard heap, the header for Chunk B sits 
    // exactly 8 or 16 bytes before the chunkB pointer.
    
    printf("\n[!] Triggering Overflow in Chunk A...\n");
    printf("Enter data (Over 32 bytes will smash Chunk B's header): ");
    
    char input[128];
    scanf("%s", input);
    strcpy(chunkA, input); // CWE-122: Heap-based Buffer Overflow

    printf("[+] Metadata corrupted. Now attempting to Free Chunk B...\n");
    printf("[*] This will likely trigger a Critical Breakpoint or Bugcheck.\n");
    
    // The Heap Manager will look at the corrupted header of Chunk B 
    // to decide how to unmount it from the free list.
    HeapFree(hHeap, 0, chunkB); 
}

int main() {
    printf("--- Heap Metadata Corruption Lab ---\n");
    lab_setup();
    return 0;
}