#! /usr/bin/env python3


from pwn import *
conn = remote('time.challs.olicyber.it',10505)

# ciclo infinito
# 01100110011011000110000101100111011110110100110000110100010111110110111001010101011011010011001101110010001100000101111100110001010111110011001101011111010100110110000100110001011101100011010001111101


from pwn import *
conn = remote('time.challs.olicyber.it',10505)
answer = ''
for i in range(200):
	print(i, "bits finora ",answer)
	while True:

		
		conn.recvuntil('> ')
		conn.sendline('1')
		conn.recvuntil('vuoi ricevere? ')
		conn.sendline(str(i))

		
		res = conn.recvline()
		# se ha un errore nel calcolo di AES nel server allora metto un 0 nella mia stringa e continuo
		# mi ritorna :()
		if res == b':(\n':
			conn.close()
			conn = remote('time.challs.olicyber.it',10505)
			answer += '0'
			break
		

		# se non si puo trasformare bene in bytes allora so che 'e RSA allora continuo
		try:
			res = bytes.fromhex(res.strip().decode())
		except:
			answer += "1"
			break
		

print(answer)
hexadecimal = hex(int(answer,2))[2:]
print(hexadecimal)

from utilities import hexToStr

print(hexToStr(hexadecimal))

# flag{L4_nUm3r0_1_3_Sa1v4}
