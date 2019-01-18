

──────────────────────────────────────[ DISASM ]──────────────────────────────────────
   0x80487d8  <toooomuch+90>             ret    
    ↓
   0x80484c0  <system@plt>               jmp    dword ptr [_GLOBAL_OFFSET_TABLE_+32] <0x8049c04>

   0x80484c6  <system@plt+6>             push   0x28
 ► 0x80484cb  <system@plt+11>            jmp    0x8048460
    ↓
   0x8048460                             push   dword ptr [_GLOBAL_OFFSET_TABLE_+4] <0x8049be8>
   0x8048466                             jmp    dword ptr [0x8049bec] <0xf7efae10>
    ↓
   0xf7efae10 <_dl_runtime_resolve>      push   eax
   0xf7efae11 <_dl_runtime_resolve+1>    push   ecx
   0xf7efae12 <_dl_runtime_resolve+2>    push   edx
   0xf7efae13 <_dl_runtime_resolve+3>    mov    edx, dword ptr [esp + 0x10]
   0xf7efae17 <_dl_runtime_resolve+7>    mov    eax, dword ptr [esp + 0xc]
──────────────────────────────────────[ STACK ]───────────────────────────────────────
00:0000│ esp  0xffc0e6fc ◂— 0x28 /* '(' */
01:0004│      0xffc0e700 —▸ 0x8049c60 (passcode) ◂— das     /* 0x6e69622f; '/bin/sh' */
02:0008│      0xffc0e704 —▸ 0xffc0e700 —▸ 0x8049c60 (passcode) ◂— das     /* 0x6e69622f; '/bin/sh' */
03:000c│      0xffc0e708 ◂— 0x0
04:0010│      0xffc0e70c —▸ 0xf7cf9e81 (__libc_start_main+241) ◂— add    esp, 0x10
05:0014│      0xffc0e710 —▸ 0xf7eb9000 (_GLOBAL_OFFSET_TABLE_) ◂— insb   byte ptr es:[edi], dx /* 0x1d7d6c */
... ↓
07:001c│      0xffc0e718 ◂— 0x0

─────────────────────────────────────────────────────────────────────────────────[ DISASM ]──────────────────────────────────────────────────────────────────────────────────
 ► 0x56555410 <system@plt>    jmp    dword ptr [ebx + 0x10] <0xf7e0e200>
    ↓
   0xf7e0e200 <system>        sub    esp, 0xc
   0xf7e0e203 <system+3>      mov    eax, dword ptr [esp + 0x10]
   0xf7e0e207 <system+7>      call   __x86.get_pc_thunk.dx <0xf7f0837d>
 
   0xf7e0e20c <system+12>     add    edx, 0x19adf4
   0xf7e0e212 <system+18>     test   eax, eax
   0xf7e0e214 <system+20>     je     system+32 <0xf7e0e220>
 
   0xf7e0e216 <system+22>     add    esp, 0xc
   0xf7e0e219 <system+25>     jmp    do_system <0xf7e0dce0>
 
   0xf7e0e21e <system+30>     nop    
   0xf7e0e220 <system+32>     lea    eax, [edx - 0x59f29]
──────────────────────────────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────────────────────────────
00:0000│ esp  0xffffccec —▸ 0x565555c1 (main+68) ◂— add    esp, 0x10
01:0004│      0xffffccf0 —▸ 0xffffcd04 ◂— '/bin/sh'
02:0008│      0xffffccf4 —▸ 0x56556fd4 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1edc
03:000c│      0xffffccf8 —▸ 0xffffcdcc —▸ 0xffffd02f ◂— 0x54554c43 ('CLUT')
04:0010│      0xffffccfc —▸ 0x56555594 (main+23) ◂— add    eax, 0x1a40
05:0014│      0xffffcd00 ◂— 0x1
06:0018│ edx  0xffffcd04 ◂— '/bin/sh'
07:001c│      0xffffcd08 ◂— 0x68732f /* '/sh' */

   0x565555bc <+63>:    call   0x56555410 <system@plt>
   0x565555c1 <+68>:    add    esp,0x10

