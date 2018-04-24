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
#host = "chall.pwnable.tw"
#port = 10100
r = remote(host, port)

input("attach in gdb and press Enter")

payload = flat([])

print(payload)

#r.recvuntil(":")
#r.sendline(payload)
#r.interactive()

