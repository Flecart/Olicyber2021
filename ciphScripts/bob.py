#! /usr/bin/env python3


from pwn import *
from base64 import b64decode

conn = remote("bob.challs.olicyber.it", 10602)



def toArrayBlocks(everyBlock):
	arrBlocks = []
	for i in range(len(everyBlock)):
		if i % 16 == 0:
			arrBlocks.append(everyBlock[i-16:i])

	arrBlocks = arrBlocks[1:]
	arrBlocks.append(everyBlock[-16:])

	return arrBlocks
# print(ans)
# print(len(ans))

baseBigBlock = "AAAAAAAAAAA" + "A" * (15*16)
baseBigBlock = baseBigBlock[:-33]
copiedStuff = "Alice: certo, eccola: flag{Sono_"
# "Alice: certo, eccola: flag{Sono_Stu"

for indexBlock in reversed(range(14)):
	print("sto lavorando sul blocco", indexBlock)
	for x in reversed(range(16)):
		print("le cose che ho trovato finora -"+ copiedStuff+"-")
		for char in range(32,127): # range dei caratteri ascii printabili
			payload = baseBigBlock  + copiedStuff +  chr(char) + "Bob: " + baseBigBlock

			conn.recvuntil("Bob: ")
			conn.sendline(payload)
			conn.recvuntil("questo messaggio!\n")
			ans = b64decode(conn.recvline().strip())
			conn.recvuntil("Riprova pure premendo 1\n")
			conn.sendline("1")
			# cose di andata e ritorno

			blocks = toArrayBlocks(ans)
			if blocks[15] == blocks[15 + 16]:
				copiedStuff += chr(char)
				baseBigBlock = baseBigBlock[:-1]

				# se ho finito esco e printo la mia risposta
				if indexBlock == 0:
					print(copiedStuff, "Ho finito tutto!")
					exit(0)
				break
			elif char == 126:
				print('Grandissimo problema al blocco', indexBlock)
				print('Di index',x)
				print('Sono riuscito a trovare le parole correnti', copiedStuff)
				exit(0)
				# problema grosso perch'e ho sbagliato impelmentazione prima
