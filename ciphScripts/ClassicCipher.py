#!/usr/bin/env python3

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
# zyxwvutsrqponmlkjihgfedcba

def generateKey():
    start = random.randint(1,25)
    key = "".join([alphabet[start:], alphabet[0:start-1]])
    return key

def encrypt(plain, key):
    ciphertext = ""
    for k in range(len(plain)):
        character = plain[k]
 
        if ord(character) <= 90 and ord(character) >= 65: #lowercase
            i = alphabet.index(chr(ord(character)+32))
            characterEncrypted = chr(ord(key[i])-32)
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            ciphertext = "".join([ciphertext,characterEncrypted])
        elif ord(character) <= 122 and ord(character) >= 97:
        	# mi ritrova l' index nell' alfabeto, praticamente conto
            i = alphabet.index(character)

            # me la cambia nella chiave
            characterEncrypted = key[i]
            
            key = "".join([key[1:], key[0]])
            # key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            ciphertext = "".join([ciphertext,characterEncrypted])
        else:
        	# se non `e un carattere me lo mette subito su.
            ciphertext = "".join([ciphertext,character])
        
    return ciphertext
def handle():
    # QUi trovo la flag
    plaintextFLAG = "xcqv{gvyavn_zvztv_etvtddlnxcgy}"
    start = 8

    # sto prendendo il giusto shift con la chiave, aveevo trovato con 
    key = "".join([alphabet[start:], alphabet[0:start]])
    print(key)
    ciphertext = encrypt(plaintextFLAG, key)
    print(ciphertext, start)
    
    return



if __name__ == "__main__":
    handle()