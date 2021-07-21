#! /usr/bin/env python3

# with open('./data', 'w') as file:
#     data = input()
#     file.write(data)


# g, p = open('./data').read().split()
# g, p = int(g, 16), int(p, 16)	

# print(g,p)

# ho messo 1 a p in modo che mandasse tutto a 0 ahahah
# Quindi conosco gi`a il valore della chaive devo solemente decrittare con aes

from Crypto.Cipher import AES 
from base64 import b64decode

encode = 'zSgtnZ26GBEmBC8ATITRonCIva6ZETGbuZKD/Q7hTDE='
decoded = b64decode(encode)

print(AES.new(bytes([0]*16), AES.MODE_ECB).decrypt(decoded))