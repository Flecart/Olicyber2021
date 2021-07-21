#! /usr/bin/env python3

# questa `e facile, la flag `e codificata in questo codice qua sotto
# probabilmente in origine era una strana matrice, ma ora faccio questo coso cos`i
import string

printable = string.printable

def controllo(flag):
	boolz = []
	boolz.append(ord(flag[0x13]) * -0xfa + ord(flag[0x13]) * ord(flag[0x13]) == -0x3d09 )
	boolz.append(ord(flag[0x12]) * -0x60 + ord(flag[0x12]) * ord(flag[0x12]) == -0x900 )
	boolz.append(ord(flag[0x11]) * -0xbe + ord(flag[0x11]) * ord(flag[0x11]) == -0x2341 )
	boolz.append(ord(flag[0x10]) * -0xca + ord(flag[0x10]) * ord(flag[0x10]) == -0x27d9 )
	boolz.append(ord(flag[0xf]) * -0xe8 + ord(flag[0xf]) * ord(flag[0xf]) == -0x3490 )
	boolz.append(ord(flag[0xe]) * -0xdc + ord(flag[0xe]) * ord(flag[0xe]) == -0x2f44 )
	boolz.append(ord(flag[0xd]) * -0xc2 + ord(flag[0xd]) * ord(flag[0xd]) == -0x24c1 )
	boolz.append(ord(flag[0xc]) * -0xdc + ord(flag[0xc]) * ord(flag[0xc]) == -0x2f44 )
	boolz.append(ord(flag[0xb]) * -0xd2 + ord(flag[0xb]) * ord(flag[0xb]) == -0x2b11 )
	boolz.append(ord(flag[10]) * -0xda + ord(flag[10]) * ord(flag[10]) == -0x2e69) 
	boolz.append(ord(flag[9]) * -0xe4 + ord(flag[9]) * ord(flag[9]) == -0x32c4 )
	boolz.append(ord(flag[8]) * -0xca + ord(flag[8]) * ord(flag[8]) == -0x27d9 )
	boolz.append(ord(flag[7]) * -0xe8 + ord(flag[7]) * ord(flag[7]) == -0x3490 )
	boolz.append(ord(flag[6]) * -0x66 + ord(flag[6]) * ord(flag[6]) == -0xa29 )
	boolz.append(ord(flag[5]) * -200 + ord(flag[5]) * ord(flag[5]) == -10000 )
	boolz.append(ord(flag[4]) * -0xf6 + ord(flag[4]) * ord(flag[4]) == -0x3b19 )
	boolz.append(ord(flag[3]) * -0xce + ord(flag[3]) * ord(flag[3]) == -0x2971 )
	boolz.append(ord(flag[2]) * -0xc2 + ord(flag[2]) * ord(flag[2]) == -0x24c1 )
	boolz.append(ord(flag[1]) * -0xd8 + ord(flag[1]) * ord(flag[1]) == -0x2d90) 
	boolz.append(ord(flag[0]) * -0xcc + ord(flag[0]) * ord(flag[0]) == -0x28a4)

	return boolz
knownFlag = ''
currentFlag = 'a' *0x13
for i in reversed(range(0x14)):
	for x in printable:
		payload = knownFlag +x + currentFlag
		coso = controllo(payload)
		if (coso[i]):
			knownFlag += x
			currentFlag = currentFlag[:-1]
			break

print(knownFlag)

# flag{d3terminante_0}
