#! /bin/python3
from pwn import *
import math
conn = remote("2048.challs.olicyber.it", 10007)
# nc  2048.challs.olicyber.it 10007
print(conn.recvline())
print(conn.recvline())

array = [b"PRODOTTO", b"DIVISIONE_INTERA", b"DIFFERENZA", b"POTENZA", b"SOMMA"]
i = 0
while(True):
	operation = conn.recvuntil(b' ', drop=False)[0:-1]
	if (operation not in array):
		print(operation)
		break;
	if (i > 1500):
		print(i)
	a = int(conn.recvuntil(b' ', drop=False))
	b = int(conn.recvuntil(b' ', drop=False))
	if operation == b"PRODOTTO":
	    conn.send(bytes(str(a*b) + '\n',encoding='utf8'))
	    # conn.send(b'\n')

	elif operation == b"SOMMA":
	    conn.send(bytes(str(a+b) + '\n',encoding='utf8'))
	    # conn.send(b'\n')
	elif operation == b"DIVISIONE_INTERA":
	    conn.send(bytes(str(math.floor((a /b))) + '\n',encoding='utf8'))
	    # conn.send(b'\n')

	elif operation == b"DIFFERENZA":
	    conn.send(bytes(str(a-b) + '\n',encoding='utf8'))
	    # conn.send(b'\n')
	elif operation == b"POTENZA":
		conn.send(bytes(str(a**b) + '\n',encoding='utf8'))
		# conn.send(b'\n')
	i += 1
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())

# #######
# zipception2
# #! /bin/python3
# import zipfile
# from tqdm import tqdm
# wordlist = "./wordlist"
# n_words = 1000000
# boolean = True
# for i in reversed(range(6)):


# 	zip_file = zipfile.ZipFile(f"{i}.zip", 'r')
# 	opened = open(wordlist, "rb")
	
# 	for word in tqdm(opened, total=n_words, unit="word"):
# 	    try:
# 	        zip_file.extractall(pwd=word.strip())
# 	    except:
# 	        continue
# 	    else:
# 	        print("[+] Password found:", word.decode().strip())
# 	        opened.close()
# 	        boolean = False
#         	break
# 	if boolean:
# 		print("not enough passowrds")
           
