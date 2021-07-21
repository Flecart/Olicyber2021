import os
# from secret import FLAG

def xor(a, b):
    return bytes([ x ^ y for x,y in zip(a,b) ])

key = os.urandom(6)
# with open("output.txt", "w") as output_file:
    # output_file.write(f"FLAG: {xor(FLAG, key * (len(FLAG)//len(key) + 1)).hex()}")

def hexToBytes(hexString):
	ans = []
	for x in range(0,len(hexString),2):
		ans.append(int(hexString[x] + hexString[x+1],16))
	return ans
with open("output.txt", "r") as f:
	stream = f.read()[:-1]
	byts = hexToBytes(stream)
	
	key = b"A\xe5U>\xa7\xb6"
	ans = xor(byts, key * (len(byts)//len(key) + 1))
	print(ans) 

