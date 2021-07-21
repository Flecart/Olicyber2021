#! /usr/bin/env python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# with open("ycomplete.txt", "r") as f:
# 	data = f.read().split("\n")


# 	lastIndex = 0
# 	for i in range(len(data)):

# 		if data[i] == "end":
# 			print(i - lastIndex -2)
# 			lastIndex = i

with open('./words.txt') as f:
    words = list(sorted([word.strip().encode('utf-8') for word in f.readlines()]))

# for x in range(len(alphabet)):
# 	alphabet[x] = "ka" + alphabet[x]	

print(alphabet)		
voluto = [3952,825,23,3,2,2,1,1,1,1,1,1,1]

def next_char(char):
    return (ord(char) + 1).to_bytes(1, 'big')

def get_words_by_prefix(prefix):
    # In un mondo ideale qui userei una struttura ad albero, ma sono troppo pigro per farlo
    # Estraggo l'ultimo carattere del prefisso
    prefix, last_char = prefix[:-1], prefix[-1].to_bytes(1, 'big')

    # Esempio: se il prefisso è mal allora voglio tutte le parole W tali per cui mal <= W < mam
    # Quindi lower_bound = mal e upper_bound = mam
    lower_bound = prefix + last_char
    upper_bound = prefix + next_char(last_char)

    return len([w for w in words if lower_bound <= w < upper_bound])
# e, o 
for char in alphabet:

	print(get_words_by_prefix(("kapelle" + char).encode("utf-8")), char)

# ans = ""
# for numero in voluto:
# 	temp = ans
# 	for char in alphabet:
# 		temp += char
# 		lunghezza = get_words_by_prefix(temp.encode('utf-8'))
# 		# print(temp, lunghezza)
# 		if numero == lunghezza:
# 			ans = temp
# 			break
# 		else:
# 			temp = ans

# print(ans)

# with open("words.txt", "r") as f:
# 	data = f.read().split("\n")

# 	lastIndex = 0
# 	for i in range(len(data)):

# 		if data[i] in alphabet and len(data[i]) == 3:
# 			print(data[i], i-lastIndex)
# 			lastIndex = i