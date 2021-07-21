#! /usr/bin/env python3

from Crypto.PublicKey import RSA

pem = open('./cert').read()

key = RSA.import_key(pem)

print(key.n, key.e)