#! /usr/bin/env python3

from pwn import *
conn = remote('time.challs.olicyber.it',10505)
answer = ''
for i in range(200):
	print(i, "bits finora ",answer)
	while True:

		# se ha un errore nel calcolo di AES nel server allora metto un 0 nella mia stringa e continuo
		try:
			conn.recvuntil('> ')
		except:
			conn.close()
			conn = remote('time.challs.olicyber.it',10505)
			answer += '0'
			break

		conn.sendline('1')
		conn.recvuntil('vuoi ricevere? ')
		conn.sendline(str(i))

		# se non si puo trasformare bene in bytes allora so che 'e RSA allora continuo
		try:
			res = bytes.fromhex(conn.recvline().strip().decode())
		except:
			# cos`i so che qui c'e' un 1
			res = "troll"
		
		if res == "troll":
			answer += "1"
			break
		

print(answer)
hexadecimal = hex(int(answer,2))[2:]
print(hexadecimal)

def hexToStr(hex):
    res = b''

    for i in range(0,len(hex),2):
        c = hex[i:i+2]
        try:
            res += bytes.fromhex(c)
        except:
            print("ho trovato non esadecimale in", hex)
            continue

    return res
    
print(hexToStr(hexadecimal))