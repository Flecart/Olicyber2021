#! /usr/bin/env python3

from base64 import b64decode
import random
def gettingCode():
	with open("output.txt", "r") as stream:
		stream = stream.read()
		decodedText = b64decode(stream)
		print(decodedText)
		# print(len(decodedText))
	return

decodedText = b'7mJP\xbc\xc8\x9b\xfcG}\xf5@\xe96\xd5\x1b\xea7\xe0\x89\xfb\xe4\xaf\x81\x84\xdf\xde*_v#\xe9'

s_box = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251, 124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203, 84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78, 8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37, 114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146, 108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132, 144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6, 208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115, 150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110, 71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27, 252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95, 96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239, 160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97, 23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]

p_box = (0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11)

def xor_with_key(block, key):
    return [k ^ b for k, b in zip(key, block)]
    
def permutation(block, box=p_box):
    new_block = [block[idx] for idx in box]
    return new_block
    
def substitution(block, box=s_box):
    new_block = [box[char] for char in block]
    return new_block

def different(byteChar,begin):
	ans = []
	for x in range(256):	
		for y in range(256):

			first = begin ^ y
			second = s_box[first]
			third = second ^ x

			if third == byteChar:
				ans.append((x,y))
	return ans

def same(byteChar,begin):
	ans = []
	for x in range(256):
		first = begin ^ x
		second = s_box[first]
		third = second ^ x
		if third == byteChar:
			ans.append(x)

	return ans

firstblock = decodedText[:16]
secondblock = decodedText[16:]
BLOCK_LENGTH = 16
for x in range(256):
	for y in range(256):

		random.seed(bytes([x,y]))
		key_expanded = random.getrandbits(BLOCK_LENGTH*8).to_bytes(BLOCK_LENGTH, 'big')
		block = xor_with_key(firstblock, key_expanded)
		block = permutation(block)
		block = substitution(block)
		block = xor_with_key(block, key_expanded)
		if block[0] == 102 and block[1] == 108:
			print(x,y,"".join([chr(i) for i in block]))


random.seed(bytes([110,111]))
key_expanded = random.getrandbits(BLOCK_LENGTH*8).to_bytes(BLOCK_LENGTH, 'big')
block = xor_with_key(secondblock, key_expanded)
block = permutation(block)
block = substitution(block)
block = xor_with_key(block, key_expanded)
print("".join([chr(i) for i in block]))

# block = decodedText[0:16]
# clearBlock = b"flag{aaaaaaaaaaa"
# # rimetto in posizione

# data = []
# for x in range(5):
# 	data.append([clearBlock[x],x,oldP_box[x]])

# keyblock = [0] * 16

# i = 0
# for x in [0, 13, 10, 7, 4]:
# 	begin = block[x]
# 	byteChar = data[i][0]

# 	if data[i][1] == data[i][2]:
# 		keyblock[i] = same(byteChar, begin)
# 	else:
# 		keyblock[i] = different(byteChar, begin)
# 	i += 1

# print(keyblock)

