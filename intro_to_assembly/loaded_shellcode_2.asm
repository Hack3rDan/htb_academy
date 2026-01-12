_start:
push   rbx
mov    dh,0x4b
mov    ebx,0x77435348
mov    ebx,0x9a4c5348
mov    ebx,0xbf264d34
cmps   DWORD PTR ds:[rsi],DWORD PTR es:[rdi]
sbb    esi,DWORD PTR [rbp+0x23467c7a]
jle    0x7fffffffda06
and    DWORD PTR [rdi+rbp*4+0x66],eax
rex.W
push rbx
rex.W
mov    ebx,0x31c05048
jno    0x7fffffffd9c8
