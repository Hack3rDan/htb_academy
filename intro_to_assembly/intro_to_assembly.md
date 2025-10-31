# Registers

| Data Registers | Description
| rax/eax/ax/al | Syscall Number/Return Values |
| rbx/ebx/bx/bl | Callee Saved |
| rcx/ecx/cx/cl | 4th arg - Loop counter |
| rdx/edx/dx/dl |3rd arg |
| r8/r8d/r8w/r8b | 5th arg|
| r9/r9d/r9w/r9b | 6th arg|
| r10 ||
| rdi/edi/di/dil | 1st arg - destination operand |
| rsi/esi/si/sil | 2nd arg - source operand |
| rbp/ebp/bp/bpl | base stack pointer |
| rsp/esp/sp/spl | current/top stack pointer |
| rip/eip/ip/ipl | instruction pointer 'call only' |

# Syscall Arguments
Description 	64-bit Register 	8-bit Register
Syscall Number/Return value 	rax 	al
Callee Saved 	rbx 	bl
1st arg 	rdi 	dil
2nd arg 	rsi 	sil
3rd arg 	rdx 	dl
4th arg 	rcx 	cl
5th arg 	r8 	r8b
6th arg 	r9 	r9b

# Linux Syscall Tables

[https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md](Syscalls)

# Function Calling Convention

## Before calling a function

1. Save registers on the stack (caller saved)
2. Pass function arguments (like syscalls)
3. Fix stack alignment
4. Get function's Return Value (in rax)

## Writing Functions

1. Saving callee saved registers (rbx and rbp)
2. Get arguments from registers
3. Align the stack
4. Return value in rax

# Shellcode requirements

1. Does not contain variables
2. Does not refer to direct memory addresses
3. Does not contain any NULL bytes \x00

- to avoid null bytes, use the appropriately sized register for your operation

# shellcode practice

- Use one of the tools to generate a shellcode that prints the contents of the '/flag.txt'

```
printf
```
