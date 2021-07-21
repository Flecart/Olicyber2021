#! /bin/python3

string = '146330605473666206330630144146575643203056327630156276630603445756314275063276665622766106033462175'
ans = ''
for i in range(len(string)):
	if i == len(string) - 1:
		print("caratteri rimanenti", string[i:])
		break
	stringa = string[i]+string[i+1]

	encoded = int(stringa, 8)
	if encoded >= 32 and encoded <=126:
		ans += chr(encoded)
		i += 1
	else:
		stringa += string[i+2]
		encoded = int(stringa, 8)
		ans += chr(encoded)
		i+=2


print(ans)