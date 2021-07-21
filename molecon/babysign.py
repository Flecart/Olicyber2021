#! /usr/bin/env python3

from pwn import remote #pip install pwntools
from hashlib import sha256
from Crypto.Util.number import bytes_to_long, long_to_bytes

def solvepow(p, n):
    s = p.recvline()
    starting = s.split(b'with ')[1][:10].decode()
    s1 = s.split(b'in ')[-1][:n]
    i = 0
    print("Solving PoW...")
    while True:
        if sha256((starting+str(i)).encode('ascii')).hexdigest()[-n:] == s1.decode():
            print("Solved!")
            p.sendline(starting + str(i))
            break
        i += 1

def exploit(p):
    # prendo chiave pubblica
    # p.recvuntil('Exit')
    # p.sendline('4')
    # p.recvuntil(': ')
    # n = int(p.recvline().strip())
    # p.recvuntil(': ')
    # e = int(p.recvline().strip())
    # print(n,e)

    # # decripto
    # p.sendline('2')

    # # payload = bytes_to_long(b'A' * 64)

    # p.sendline('A'*64)

    # p.recvuntil('Exit')
    # p.recvline()
    # ciphertext = int(p.recvline().strip().decode(),16)
    # print(ciphertext)
    
    # plaintext = pow(ciphertext, e, n)
    # hash = bytes_to_long(sha256(b'A'*32).digest())

    # soluzione = long_to_bytes(hash ^ plaintext)
    # print(soluzione)
    p.interactive()

if __name__ == '__main__':
    p = remote('challs.m0lecon.it', 7012)
    solvepow(p, n = 5)
    exploit(p)
