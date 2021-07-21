#! /usr/bin/env python3

from pwn import *
import json
from base64 import b64encode, b64decode
import binascii
conn = remote("based.challs.olicyber.it", 10600)


conn.recvuntil("Converti questo ");
stringa = conn.recvline().strip();

da = stringa.split()[0]
cosa = stringa.split()[1][:-1]

js = json.loads(conn.recvline().strip())
codice = js['message']



def sendAnswer(answer):
	answer = {"answer": answer.decode()}
	answer = json.dumps(answer)
	conn.sendline(answer)
	conn.interactive()

if da == b'da':
	# print('what')
	if cosa == b'esadecimale':
		# dfasdfasf
		answer = b''
		for x in range(0,len(codice),2):
			c = codice[x:x+2]

			answer += bytes.fromhex(c)
		sendAnswer(answer)
		
	elif cosa == b'base64':
		answer = b64decode(codice)
		sendAnswer(answer)

	elif cosa == b'binari':
		answer = binascii.b2a_uu(codice)
		sendAnswer(answer)
else:

	if cosa == b'binari':
		answer = binascii.a2b_uu(codice)
		sendAnswer(answer)
	elif cosa == b'base64':
		answer = b64encode(codice.encode())
		sendAnswer(answer)
	elif cosa == b'esadecimale':
		answer = ''
		for x in codice:
			answer += hex(ord(x))[2:]
		sendAnswer(answer.encode())
		# dsafasgfas
	# fai qualcosaltro

# else:
	# fai qualcosaltro