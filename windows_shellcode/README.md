# TODO

- 05 FEB: Compiles and successfully runs calc.exe. At this point, I need to
  modify the code to run a shell (cmd.exe) and then we need to make it a reverse
shell.

- [ ] change from calc.exe to cmd.exe - keep in mind stack alignment
- [ ] add a call to initiate the reverse shell
- [ ] script the assembling, and objdump formatting
- [ ] MAYBE: submit ticket to the resource guy and let him know the cmpsb doens't work on win11


- [X] Currently getting a segfault. I think its due to stack alignment
- [X] recompile the shellcode with the WinExec chars fixed on the stack.

04Feb: Fixed seg fault - stack alignment appeared to be the issue
Now the address of WinExec is being calculated incorrectly. My hunch
is that the problem is in the .found section. Doing the math with eax looks
wrong.

# Resources
Great resource to get understand the process of building shellcode on Windows:

https://idafchev.github.io/exploit/2017/09/26/writing_windows_shellcode.html



# Turn assembly into Binary

## Compile with nasmA

```nasm -f win32 shellcode.asm -o shellcode.obj```

## Link with ld

```ld -o shellcode.exe shellcode.obj --entry .start```

## Extract with objdump

```objdump -d shellcode.exe```

## Use Vim to turn into "c-string"

This will take the objdump output and turn it into a c-string format for compiling.

Each step is discrete in these directions, but you could script the whole thing.

### Remove the addresses at the front of the line

```:%s/^\s*\S\+:\s*//```

^: Anchors the match to the start of the line.

\s*: Handles any leading whitespace (just in case).

\S\+: Matches one or more non-whitespace characters (your address 401072).

:: Matches the literal colon.

\s*: Matches all the whitespace immediately following the colon.

//: Replaces it with nothing (deletes it).

### Remove the whitespace and instructions after the opcodes

```:%s/\s\{2,}.*$//```

```\s\{2,}``` matches on two or more whitespace characters
```.*``` everything to the end of the line
```$``` anchors at the end of the line so the match will be the first one at the end

### Add the '\x' before each opcode

```%s/\(\x\+\)/\\x\1/g```


### Delete whitespace

```:%s/\s//g```


### Remove newline

```:%s/\n//g```

### Wrap at 80 characters and in quote

```:%s/.\{1,80\}/"&"\r/g```

### Copy the entire buffer to the system clipboard

```:%y+```

## Use GCC to compile the test program including shellcode

```gcc -Wl,--nxcompat=no -Wl,--dynamicbase=no -fno-stack-protector -m32 -o shellcode.exe -g opcodes.c```
