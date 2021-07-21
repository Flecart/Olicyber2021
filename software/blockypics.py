#! /usr/bin/env python3

# from pwn import *
from Crypto.Cipher import AES
# chiavi.txt
# primo coso
# 0x7fffffffdf70: 0x91    0x45    0x16    0xbe    0xfb    0xf1    0xe0    0x7c
# 0x7fffffffdf78: 0xdb    0x2d    0x0e    0x32    0x1d    0xdc    0x94    0xe3
# 0x7fffffffdf80: 0xae    0x86    0x23    0xc3    0x7e    0xf9    0xd4    0xf9
# 0x7fffffffdf88: 0xd2    0x93    0x2e    0x58    0xd3    0xa1    0xe5    0x98
# 0x7fffffffdf90: 0x16    0x64    0x49    0x89    0xcd    0x45    0x47    0xbc
# 0x7fffffffdf98: 0x6a    0x62    0x11    0xa0    0x94    0x69    0xb2    0xfb

# secondo 
# 0x7fffffffdf70: 0xcb    0x24    0x47    0x32    0xa9    0xcc    0x5f    0xdc
# 0x7fffffffdf78: 0x1b    0x1c    0xd4    0x2c    0x74    0x21    0xd2    0x5b
# 0x7fffffffdf80: 0x3c    0x81    0x88    0x81    0xc2    0xdd    0x78    0x7d
# 0x7fffffffdf88: 0x90    0x85    0xd7    0x31    0x41    0x8a    0xb9    0x0a
# 0x7fffffffdf90: 0xec    0x5a    0x9a    0x6b    0x72    0x08    0xa0    0x8a
# 0x7fffffffdf98: 0xa6    0x9f    0x2d    0x09    0x08    0x8b    0x3c    0x33

# terzo
# 0x7fffffffdf70: 0xa8    0x91    0xc1    0x81    0xc3    0x03    0x27    0x8a
# 0x7fffffffdf78: 0x3b    0x5a    0xc8    0x9f    0xc1    0x88    0x42    0x97
# 0x7fffffffdf80: 0x95    0x5e    0xfe    0x2b    0xa4    0x74    0x6b    0x57
# 0x7fffffffdf88: 0x7b    0x3d    0xc8    0x74    0xc9    0x30    0xfc    0xcc
# 0x7fffffffdf90: 0x4f    0x7d    0x63    0x79    0x74    0x93    0xcc    0x2d
# 0x7fffffffdf98: 0xd9    0x9b    0x7e    0x99    0x33    0x0a    0x81    0xd8

# quarto
# 0x7fffffffdf70: 0x7b    0xb8    0xe5    0x1d    0xfa    0x3e    0x3f    0x10
# 0x7fffffffdf78: 0x20    0x52    0xcf    0x3b    0xd5    0xa0    0xed    0xb9
# 0x7fffffffdf80: 0x7c    0xd1    0x4f    0x30    0x04    0x28    0x1b    0xea
# 0x7fffffffdf88: 0xa4    0x3b    0x27    0xde    0x1b    0x36    0xc6    0xe8
# 0x7fffffffdf90: 0xb2    0x6f    0x4c    0x6c    0x8a    0x46    0x88    0x39
# 0x7fffffffdf98: 0xb5    0xee    0xb1    0x24    0x05    0x66    0x0f    0x61

# quinto
# 0x7fffffffdf70: 0x82    0x05    0xa9    0xc6    0xbe    0x24    0x1b    0x42
# 0x7fffffffdf78: 0x88    0x8f    0x20    0xff    0xb2    0xd6    0x1d    0x59
# 0x7fffffffdf80: 0x4d    0x57    0xc0    0xd0    0x47    0x31    0x37    0x99
# 0x7fffffffdf88: 0x58    0x71    0xa9    0x33    0x7a    0x3f    0x0a    0x84
# 0x7fffffffdf90: 0x0e    0xc2    0x6e    0x84    0x07    0x0c    0xf6    0x0b
# 0x7fffffffdf98: 0x70    0xf4    0x00    0x4b    0xb4    0x37    0xf3    0x3a

# flag{y_reVErs1ng-WHeN-yA_C4n-b3-LAZY}
def transformHex(array):
    ans = b''
    for x in array:
        ans += bytes.fromhex(x[2:]) # tolgo 0x e metto incontrario per endianess
    return ans


# set up key and iv
with open('chiavi.txt', 'r') as f:
    with open('picsdata.txt','r') as foto:
        print(foto.readline())
        for x in range(5):
            f.readline()
            iv = transformHex(f.readline().split()[2:] + f.readline().split()[2:])
            print(iv)
            key = transformHex(f.readline().split()[2:] + f.readline().split()[2:] + f.readline().split()[2:] + f.readline().split()[2:])
            print(key)
            
            f.readline()

            print(key.hex(),iv.hex(), AES.block_size)
            cipher = AES.new(key, AES.MODE_CBC, iv)

            # main
        
            
            
            print(foto.readline())
            ciphredData = bytes.fromhex(foto.readline())
            with open('finalImage', 'ab') as end:
                end.write(cipher.decrypt(ciphredData))
                print('scritto con successo',x)
#     print(f.readline())
#     f.readline()
#     print(f.readline())
#     f.readline()
#     print(f.readline())
#     f.readline()
#     print(f.readline())
#     f.readline()
#     print(f.readline())
# conn = remote('blockypics.challs.olicyber.it', 10805)
# conn = process('./pics')
# with open('picsdata.txt','wb') as f:
#     while True:
#         f.write(conn.recvline())
# while True:
#     conn.recvline()
#     print(conn.recvline())
# file = conn.recvline()
# conn.interactive()https://imgur.com/I1PmZD
