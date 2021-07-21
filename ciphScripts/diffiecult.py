#! /usr/bin/env python3

from Crypto.Cipher import AES
from pwn import *

conn = remote("diffiecult.challs.olicyber.it", 10504)

conn.recvuntil("p: ")
primeNum = 19725626458234324435564699212868764963975518726541188745821495412312099107034699007999474899466458855531011363137231823861818075431228371605717093410117740072524206039965612674127382317668138170128900470249853330679729253714352968547876116313581372890930378283002355843776702883908824482097431083730889323784187421392467305343048727366636380542958473763870498175623168044823215724094799962859909026836863294425042409041581030860392815179041111562111496231813433011601373901591824652442694137666647978707904199246857625680083371244741101667942024581988641071636105009107583947870251674110447079466511109718222337853147
conn.sendline(str(primeNum))

conn.recvuntil("g: ")
generatore = 2
conn.sendline(str(generatore))


conn.recvuntil("per favore. ")

chiavePrivata = 5
chiavePubblica = pow(generatore, chiavePrivata, primeNum)
conn.sendline(str(chiavePubblica))

conn.recvuntil("Ecco la mia chiave pubblica. ")
alicePubblica = int(conn.recvline().strip(),16)

exchange = pow(alicePubblica,chiavePrivata,primeNum)
exchange = bytes.fromhex(hex(exchange)[2:])[:16]
print(exchange)

conn.recvuntil("IV: ")
iv = bytes.fromhex(conn.recvline().strip().decode())
conn.recvuntil("msg: ")
msg = bytes.fromhex(conn.recvline().strip().decode())

cipher = AES.new(exchange, AES.MODE_CBC,iv)
plaintext = cipher.decrypt(msg)
print(plaintext)