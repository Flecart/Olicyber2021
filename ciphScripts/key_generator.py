#!/usr/bin/env python3

from hashlib import sha256
from datetime import datetime
import random


# 2021-03-21 17:37:40

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')

def generate_secure_key():
	# date_time_obj = datetime.strptime('2021-03-21 17:37:40', '%Y-%m-%d %H:%M:%S')


	# timestamp: 			1616373460.0
	# timestamp corretto:	1616344660
	# ts = int(datetime.timestamp(datetime(2021, 3, 21, 17, 37, 40)))
	ts = 1616344660
	h = sha256(int_to_bytes(ts)).digest()

	seed = int_from_bytes(h[32:])
	key = h[:32]
	random.seed(seed)
	for _ in range(32):
	    key += bytes([random.randint(0, 255)])

	return key		

key = generate_secure_key()
print(key)

# def xor(a,b):
# 	res = []
# 	for i in range(len(b)):
# 		res.append(b[i] ^ k[i % len(k)])


# with open('flag.enc', 'rb') as f:
# 	with open('out', 'wb') as o:

with open("flag.enc", "rb") as f:
    stream = f.read()

ans = b""
for x in range(len(stream)):
    ans += bytes([key[x % 64] ^ stream[x]])

print(ans[:20])
with open("aaaaaa.txt", "wb") as fa:
   fa.write(ans)