#! /usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Util.number import GCD


def save(key,file):
	with open(file, 'wb') as f:
		f.write(key.exportKey())

def open_key(file):
	with open(file, 'r') as f:
		key = RSA.import_key(f.read())
	n = key.n
	return n


root = open_key('root.pem')


# looking for common primes, to get root linke
for i in range(1,51):
	filename = f'keys/key_{i}.pem'

	n = open_key(filename)
	g = GCD(n,root)
	if g!= 1:

		break

p = g
q = root // p


# standard public
e = 0x10001
d = pow(e,-1, (p-1)*(q-1))

# openssl format key
key = RSA.construct((root, e, d, p, q))

save(key, 'private.pem')