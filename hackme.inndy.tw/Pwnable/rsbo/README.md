# rsbo

open(flag_path, 0x0)
start_0
read(file_descript, my_buffer, flag_size)
start_0
write(fd_stdout, my_buffer, flag_size)

## normal calling ORW function
```
 ► 0x80485a2 <init+21>    call   open@plt <0x8048420>
        file: 0x80487d0 ◂— '/home/ctf/flag'
        oflag: 0x0
        vararg: 0xf7ffdaf8 —▸ 0xf7ffda9c —▸ 0xf7fcf3e0 —▸ 0xf7ffd940 ◂— 0x0
```
```
 ► 0x80485bf <init+50>    call   read@plt <0x80483e0>
        fd: 0xffffffff
        buf: 0xffffccb4 ◂— 0x0
        nbytes: 0x10
```
```
 0x8048729 <main+170>           call   write@plt <0x8048450>
        fd: 0x1
        buf: 0xffffccf0 ◂— 0x410a41 /* 'A\nA' */
        n: 0x3
```

## shuffle
前面的padding全部壓\x00 就有機會把for迴圈的上線也換成0

# rsbo 2
mov rbp to buffer_0
read to buffer_0
mov rsp to buffer_0

mov rbp to buffer_1
write write_libc
read to buffer_1
mov rsp to buffer_1

mov rbp to buffer_0
call system
...

