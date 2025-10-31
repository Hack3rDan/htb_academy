#!/bin/bash

filename="${1%%.*}" # remove .s extension

nasm -f elf64 ${filename}".asm"
ld -o ${filename}".elf" ${filename}".o"
[ "$2" == "-g" ] && gdb -q ${filename}".elf" || ./${filename}".elf"
