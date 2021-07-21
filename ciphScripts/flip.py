#! /usr/bin/env python3



from pwn import *
from base64 import b64decode, b64encode

conn = remote("flip.challs.olicyber.it", 10603)

conn.recvuntil("lascia questo posto!!!")
conn.sendline('1')
conn.recvuntil('Messaggio: ')
conn.sendline('Dammi la flaaag!')

conn.recvuntil("Ecco qui la tua richiesta: ")

comando = conn.recvline().decode('utf-8').strip()

conn.recvuntil("IV: ")

IV = conn.recvline().decode('utf-8').strip()
print(IV)


iv = b64decode(IV)
af = b'{"admin": false,'
av = b'{"admin": true ,'

ive = iv

for i in range(len(af)):
	ive = ive[:i] + bytes([ive[i] ^ af[i] ^ av[i]]) + ive[i+1:]

ive = b64encode(ive)
print(ive, IV)
conn.recvuntil("lascia questo posto!!!")
conn.sendline('2')
conn.recvuntil("Inserisci un ordine: ")
conn.sendline(comando)
conn.recvuntil("IV: ")
conn.sendline(ive)
conn.interactive()
# res = conn.recvuntil("lascia questo posto!!!")
# print(res)
conn.close()
