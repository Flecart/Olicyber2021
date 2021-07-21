#! /usr/bin/env python3

from math import gcd
from pwn import *
from binascii import hexlify
from Crypto.Cipher import AES

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount



conn = remote('rsa.challs.olicyber.it', 10300)

conn.recvuntil("fattore primo (p): ")
p = int(conn.recvline().strip())
conn.recvuntil("fattore primo (q): ")
q = int(conn.recvline().strip())
conn.recvuntil("esponente pubblico (e): ")
e = int(conn.recvline().strip())

print(p,q,e)

n = p*q
phi = (p-1) * (q-1)
d = pow(e,-1,phi)

conn.sendline(str(n))
conn.sendline(str(phi))
conn.sendline(str(d))
conn.recvuntil("la stringa ")
plaintext = conn.recvuntil(":")[1:-2]
plaintext = int(hexlify(plaintext),16)
ciphertext = (plaintext ** e) % n
conn.sendline(str(ciphertext))


conn.recvuntil("IV: ")
iv = bytes.fromhex(conn.recvline().strip().decode())
conn.recvuntil("CHIAVE: ")
key = int(conn.recvline().strip(),16)
conn.recvuntil("TOKEN: ")
token = bytes.fromhex(conn.recvline().strip().decode())

print(key)
key = pow(key,d,n)

print(iv,key,token)


cipher = AES.new(key.to_bytes(16,'big'), AES.MODE_CBC,iv)
plaintext = cipher.decrypt(token)
print(plaintext)