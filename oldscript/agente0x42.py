#! /usr/bin/env python3
string = "704e34bbff99f3fe"
string2= "6c00fad8ae0d6015"


otherstring1 = "70 4e 34 bb ff 99 f3 fe".split(" ")
otherstring2 = "6c 00 fa d8 ae 0d 60 15".split(" ")

ciph = "502fee1138e7e3846f3aaf4334b3b38a7a28ab113cf5e7826a2fe24330f3f685682bee5329a0a1c73c27a24322e1fccb6c27af0d3eb4e08e712cbc0271e4f6997a2bba173eb8b3877d6eaf1625fbe1826634a7023cfbb38a3c3ebc0c32f1f78e6e2be0695bf2ff8a7b35a6530ef8a7b46e7ffb1361a1a4df3011a3570ee5e6df7011fd3c3da0cc8f2c23fa0d35a0ac9616440a46696e6520636f6d756e6963617a696f6e650a"

key = [28, 78, 206, 99, 81, 148, 147, 235]

ans = ""
for i in range(0,len(ciph),2):
	char = ciph[i] + ciph[i+1]
	char = int(char,16)
	numbKey = int(i/2)
	ans += chr(key[numbKey % 8] ^ char)
	
print(ans)

# Prendere la chiave
# for x in range(len(otherstring2)):
# 	key.append(int(otherstring2[x],16) ^ int(otherstring1[x],16))

# print(key)

# ROBA BRUTTA
# constant = 4696478755256956
# # 70 4e 34 bb ff 99 f3 fe
# # 6c 00 fa d8 ae 0d 60 15
# a1 = int(string,16)
# a2 = int(string2,16)
# diff = a1 - a2
# print(a1)
# print(a2)
# print(diff/0x42)

# print(hex(diff))

# string = "AAAABAAAAAAAABAABBBAABBABABAAABAABABAABAABBBABAABBAAAAABAABABAABBBBAAA"

# count = 0
# for x in range(1, len(string)):
# 	if string[x-1] == string[x]:
# 		count += 1
# 	else:
# 		print(count+1, end=" ")
# 		count=0
# print(len(string))
# seguenze = "4 1 8 1 2 3 2 2 1 1 1 1 3 1 2 1 1 1 2 1 2 3 1 1 2 2 5 1 2 1 1 1 2 4 3"

# 70 4e 34 bb ff 99 f3 fe
# 6c 00 fa d8 ae 0d 60 15


# 70 4e 34 bb ff 99 f3 fe
# 6c 00 fa d8 ae 0d 60 15