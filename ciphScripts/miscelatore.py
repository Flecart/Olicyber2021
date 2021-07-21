#! /usr/bin/env python3

from pwn import *


conn = remote("sme.challs.olicyber.it", 10506)

conn.sendline("A" * 64)
conn.recvuntil("Ciphertext: ")
cipher1 = conn.recvline().decode('utf-8').strip()

cipher1 = bytes.fromhex(cipher1)

conn.close()
# ____________________________________
conn = remote("sme.challs.olicyber.it", 10506)

conn.sendline("A" * 64)
conn.recvuntil("Ciphertext: ")
cipher2 = conn.recvline().decode('utf-8').strip()

cipher2 = bytes.fromhex(cipher2)
conn.close()

longAs = (b'A' * 131).hex().encode()


# So da quanto abbiamo detto finora che con questo lunghissimo xor mi tolgo tutto otp, e mi mette in chiaro anche parte della
# flag in quanto ho xorato due volte la flag
def xor(primo,secondo, terzo):
	return bytes([x^y^z for x,y,z in zip(primo, secondo,terzo)])

ans = xor(cipher1, cipher2, longAs).decode("ascii", 'ignore') 

# nel codice sorgente fa hex due volte, questo `e solamente un altro hex per tutti i numeri possibili
# Mi ritrovo ancora un hex che pero con buone probabilit`a dovrebbe avere dentro di se la flag
# Ora devo solamente ritrasformarlo in una stringa leggibile e ho fatto tutto quello che dovevo fare
# per risolvere la challenge



res = b''
for i in range(0, len(ans), 2):
	c = ans[i:i+2]
	try:
		res += bytes.fromhex(c)
	except:
		continue


print(res)