#! /usr/bin/env python3
# import os
# import signal
# from Crypto.Cipher import AES
# from Crypto.Util.number import long_to_bytes
# from pwn import *
# # TIMEOUT = 300

# seed = os.urandom(16)
# def xor(a, b):
#     return bytes(x^y for x,y in zip(a,b))

# def pad(m):
#     if len(m)%48 == 0:
#         return m
#     return m + bytes([48-len(m)%48])*(48-len(m)%48)


# # nop = b'\x00' * 16

# def fill(byte):
#     if len(byte) < 16:
#         return b'\x00'*(16-len(byte)) + byte
#     else:
#         return byte

# # def check(byte):



# conn = remote("soundofsystem.challs.jeopardy.olicyber.it",15000)
# bruteforce = fill(long_to_bytes(0x80))
# payload = xor(xor(b"show_flag'''''''",b"''''''''''''''''"),bruteforce) + bruteforce*2
# print(pad(payload), len(pad(payload)))


# conn.sendlineafter('> ',payload)

# res = conn.recvline()
# if b'error' not in res:
#     print(res)
#     conn.interactive()
# conn.interactive()
import os
import signal
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes

# TIMEOUT = 300

seed = os.urandom(16)
def xor(a, b):
    return bytes(x^y for x,y in zip(a,b))

def pad(m):
    if len(m)%48 == 0:
        return m
    return m + bytes([48-len(m)%48])*(48-len(m)%48)


# nop = b'\x00' * 16

def fill(byte):
    if len(byte) < 16:
        return b'\x00'*(16-len(byte)) + byte
    else:
        return byte

# def check(byte):

from pwn import *

conn = remote("soundofsystem.challs.jeopardy.olicyber.it",15000)

payload = b"''''''''''''''''" +b"show_flag'''''''"+b"''''''''''''''''"
print(pad(payload), len(pad(payload)))


conn.sendlineafter('> ',payload)
# flag{PCBC_mode_is_not_safe!}
# res = conn.recvline()
conn.interactive()