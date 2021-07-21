#! /usr/bin/env python3
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES

# z che mi scelgo io, non capisco perch'e con z = 17 non funzionava
z = 19725626458234324435564699212868764963975518726541188745821495412312099107034699007999474899466458855531011363137231823861818075431228371605717093410117740072524206039965612674127382317668138170128900470249853330679729253714352968547876116313581372890930378283002355843776702883908824482097431083730889323784187421392467305343048727366636380542958473763870498175623168044823215724094799962859909026836863294425042409041581030860392815179041111562111496231813433011601373901591824652442694137666647978707904199246857625680083371244741101667942024581988641071636105009107583947870251674110447079466511109718222337853147

# QUesto `e un attacco MITM, molto pericoloso, ecco perch'e io ti posso prendere le tue informazioni delle banca in questo modo loool
# Comunque
# A me interessa solamente il messaggio di alice, quindi modifico solo la rispostaverso di lei, 
# anche se in casi reali lo farei ad entrambi e resterei ad ascoltare solamente allora
# comunque prendo il p che si sono mandati e lo uso per creare una Z comune ad entrambi.
# allora so che aliche ha Z**a e bob Z**b come chiavi che usano per criptare le informazioni
# Io allora conosco la chiave che ho mandato ad alice e la uso per decrittare il messaggio 
# che originariamente vuole mandare a bob. Cos`i ho la flag


# p che ho intercettato
p = 'bd9da9dd8f0307ca82ffa52d4477b3e03738d1362ed9160f1430c5d7bb22a9a3'
p = int(p,16)
g = 2
base = pow(g,z,p)

#printa fuori il Z che mi sono calcolato
print(hex(base)[2:])

# queste sono altre intercettazioni
ciphertext = bytes.fromhex('d5c54655849e46987553fa633f3ba4251797ad6d410d494941588d40bbc4d8ad6b423a3e8609fa020884174e64588cce')
iv = bytes.fromhex('943da2319128c7fe49adafd51ffc7557')
A = int('41aaa2fa888b8d80f644f4d1d0c973c77080ec78f1935673bf6733d3f91097da',16)


# mi ricavo la chiave con metodo classico
key = long_to_bytes(pow(A, z, p))


# decifro ed `e fatta
cipher = AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext)

print(cipher)