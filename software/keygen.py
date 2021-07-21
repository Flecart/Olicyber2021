#! /usr/bin/env python3

# queste sono due funzioni che ho reversato easy
def makeSerial( param_1):
	
	firstpart = "".join(pairStrings(param_1[0x12:],param_1[9:]));
	secondpart = "".join(pairStrings(param_1,param_1[0x12:]));
	thirdpart = "".join(pairStrings(param_1[9:],param_1));
	# print(firstpart)
	return firstpart + secondpart + thirdpart

def pairStrings(param_2, param_3):
	param_1 = [0] * 16
	counter3 = 0;
	counter1 = 0;
	counter2 = 0;
	while (counter1 < 8 or (counter2 < 8)):
		if ((counter3 & 1) == 0):
			param_1[counter3] = param_2[counter1] 
			counter3 = counter3 + 1;
			counter1 = counter1 + 1;
		else:
			param_1[counter3] = param_3[counter2];
			counter3 = counter3 + 1;
			counter2 = counter2 + 1;
	return param_1

from pwn import *

# conn = process('./keygenme')
conn = remote('keygenme.challs.olicyber.it',10017)
conn.recvuntil('id: ')

serial = conn.recvline().strip().decode()
print(serial)
payload = makeSerial(serial)
conn.recvuntil('chiave.')
conn.sendline(payload.encode() + b'\x00')

conn.interactive()
# flag{3z_l1c3n53_4_3v3ry0n3}