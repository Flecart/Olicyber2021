#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

a = 3
b = 8
p = 159043501668831001976189741401919059600158436023339250375247150721773143712698491956718970846959154624950002991005143073475212844582380943612898306056733646147380223572684106846684017427300415826606628398091756029258247836173822579694289151452726958472153473864316673552015163436466970719494284188245853583109
g = p-1

flag = "b5609cfbad99f1b20ec3a93b97f379d8426f934ffcb77d83ea9161fefa78d243"

def getDHkey():
    A = pow(g,a,p)
    B = pow(g,b,p)
    K = pow(B,a,p)

    return K

def handle():
	# ho modificatro solamente questa funzione qua + g-1 che e' praticamente wilson
	keyExchanged = str(getDHkey())
	decryptedFlag = decrypt(bytes.fromhex(flag),keyExchanged).hex()

	res = b''

	for x in range(0, len(decryptedFlag),2):
		c =decryptedFlag[x:x+2]
		res += bytes.fromhex(c)

	print("Il messaggio decriptato è: {0}".format(res))
	return;

def fakePadding(k):
    if (len(k) > 16):
        raise ValueError('La tua chiave è più lunga di 16 byte')
    else:
        if len(k) == 16:
            return k
        else:
            missingBytes = 16 - len(k)
            for i in range(missingBytes):
                k = ''.join([k,"0"])
            return k

def encrypt(f,k):
    key = bytes(fakePadding(k),"utf-8")

    cipher = AES.new(key, AES.MODE_ECB)
    encryptedFlag = cipher.encrypt(pad(f, AES.block_size))
    return encryptedFlag

def decrypt(f, k):
    
    key = fakePadding(str(k))
 
    chiave = bytes(key, "utf-8")
    cipher = AES.new(chiave, AES.MODE_ECB)
    decryptedFlag = cipher.decrypt(f)
    return decryptedFlag

if __name__ == "__main__":
    handle()