#! /usr/bin/env python3

from pwn import * 

# PRENDERE PRIMA PARTE DELLA FLAG


def xor(a,b,c):
	return bytes([x ^ y ^ z for x,y,z in zip(a,b,c)])	

conn = remote("berserker.challs.olicyber.it", 10507)
currentString = b''
# {Pr06r4mMing_
knownFlag = b'm4ke5_M3_4n6Ry}'
for i in range(17):
	# printo di controllo progressi
	print("sto scoprendo quanto vale la", i)

	# gestire gli input che ricevo dal server
	conn.recvuntil("> ")
	conn.sendline("1")
	conn.recvuntil("Come ti chiami? ")

	# controllo cosa c' `e nei blocci, in particolare io voglio che ci sia solamente una lettera
	# nuova in ogni blocco.
	nome = "A" * (5 + i)

	conn.sendline(nome)
	conn.recvuntil("sessione cifrato:")
	sessione = bytes.fromhex(conn.recvline().strip().decode())
	iv = sessione[-16:]
	target = sessione[-32:-16]
	c2 = sessione[-48:-32]

	# in pratica sono parti conosciute del blocco, mi aiutano a riempirlo in modo controllato
	offset = 15 - (i)

	for x in range(256):
		brutePayload = bytes([x]) + currentString + knownFlag[:offset]

		# Questo `e il pezzo principale del codice
		# devo fare xor con iv cosi me lo tolgo anche dopo
		# sto neutralizzando il CBC in questo modo
		# poi devo fare xor con c2, che sarebbe il ciphertext2, in modo che io possa
		# simulare un passaggio di crittazione precedente, quando mi registro
		# poi confronto i blocchi, che devono essere uguali e voil`a
		brutePayload = xor(iv, brutePayload,c2)
		conn.recvuntil("> ")
		conn.sendline("2")
		conn.recvuntil("da cifrare (hex): ")
		conn.sendline(brutePayload.hex())
		conn.recvuntil("cifrato: ")
		ans = bytes.fromhex(conn.recvline().strip().decode())
		iv = ans[-16:]
		res = ans[:16]

		# se sono riuscito a trovare un blocco giusto mi fa questo
		if res == target:
			currentString = bytes([x]) + currentString
			print(currentString)
			break

# SECONDA PARTE DELLA FLAG
# da eseguire prima di quell' altra, cambiano pochi valori....
#####################
# def xor(a,b,c):
# 	return bytes([x ^ y ^ z for x,y,z in zip(a,b,c)])	

# conn = remote("berserker.challs.olicyber.it", 10507)
# currentString = b'}'
# for i in range(14):

# 	print("sto scoprendo quanto vale la", i)

# 	conn.recvuntil("> ")
# 	conn.sendline("1")
# 	conn.recvuntil("Come ti chiami? ")


# 	nome = "A" * (7+i)
# 	conn.sendline(nome)
# 	conn.recvuntil("sessione cifrato:")
# 	sessione = bytes.fromhex(conn.recvline().strip().decode())
# 	iv = sessione[-16:]
# 	target = sessione[-16:]
# 	c2 = sessione[-32:-16]

# 	offset = 16 - (7 + i - 5)

# 	for x in range(256):
# 		brutePayload = bytes([x]) + currentString + bytes([offset]*offset)
# 		brutePayload = xor(iv, brutePayload,c2)
# 		conn.recvuntil("> ")
# 		conn.sendline("2")
# 		conn.recvuntil("da cifrare (hex): ")
# 		conn.sendline(brutePayload.hex())
# 		conn.recvuntil("cifrato: ")
# 		ans = bytes.fromhex(conn.recvline().strip().decode())
# 		iv = ans[-16:]
# 		res = ans[:16]
# 		if res == target:
# 			currentString = bytes([x]) + currentString
# 			print(currentString)
# 			break
