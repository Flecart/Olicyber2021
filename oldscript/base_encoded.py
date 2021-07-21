#! /bin/python3

# nc based.challs.olicyber.it 10600
from pwn import *
import json
import base64

# 65-90quit
# 97-122


# 146330605473666206330630144146575643203056327630156276630603445756314275063276665622766106033462175

# Prende la risposta, la trasforma in JSON e la manda al server
def trimAndSend(line):
	dict= {"answer": line}
	js = bytes(str(json.dumps(dict)), 'utf-8')
	conn.sendline(js)


conn = remote("based.challs.olicyber.it", 10600)

# Questi sono utili a mettere fuori gioco le linee iniziali
conn.recvline()

#Non printano niente
i = 0;
while(True):
	
	conn.recvline()	
	first = conn.recvline()

	if first != b'Ottimo!\n' and i > 1:
		print(first)
		break

	conn.recvline()

	# Le tre linee con le istruzioni
	firstline = conn.recvline()
	jsline = conn.recvline()
	# print(" io sono una linea di debug", jsline)
	secondline = conn.recvline()

	# Estrae l'operazione dalla linea
	temp = firstline.split()

	operation = temp[3][0:-1]
	andata = False
	if temp[2] == b'a':
		andata = True

	js = json.loads(jsline)
	data = js["message"]

	
	if operation == b'base64' and andata:	# testato funziona fino al print di debug
		message_bytes = data.encode('ascii')
		base64_bytes = base64.b64encode(message_bytes)
		answer = base64_bytes.decode('ascii')
		trimAndSend(answer)

	elif operation == b'base64' and not andata: # testato funziona fino al print di debug
		message_bytes = data.encode('ascii')
		base64_bytes = base64.b64decode(message_bytes)
		answer = base64_bytes.decode('ascii')
		trimAndSend(answer)

	elif operation == b'binari' and andata: # testato funziona fino al print di debug
		array =  [x for x in bytearray(js["message"], 'utf-8')]
		bytess = [format(x, 'b') for x in array]
		answer = ''
		for x in bytess:
			if len(x) < 8:
				x += "0" * (8 - len(x))
			answer += x
		if (answer[len(answer)-1] == '0'):
			answer = answer[0:-1]

		trimAndSend(answer)

	elif operation == b'binario' and not andata: # Boh escono cose strane, con bytes non rappresentabili
		data = "0" + data
		n = 8
		listaBytes = ["0b" + data[i:i+n] for i in range(0, len(data), n)]
		answer = ''
		for binario in listaBytes:
			answer += chr(int(binario,2))
		
		trimAndSend(answer)

	elif operation == b'esadecimale' and andata: # testato funziona fino al print di debug
		answer = ''.join(hex(ord(x))[2:] for x in data)
		trimAndSend(answer)

	elif operation == b'esadecimale' and not andata: # testato funziona fino al print di debug
		answer = ''.join([chr(int(''.join(c), 16)) for c in zip(data[0::2],data[1::2])])
		trimAndSend(answer)

	i += 1

print(conn.recvline())
print(conn.recvline())
print(conn.recvline())


print(conn.recvline())
print(conn.recvline())
print(conn.recvline())	

# #! /bin/python3

# # nc based.challs.olicyber.it 10600
# from pwn import *
# import json
# import base64

# # 65-90
# # 97-122

# #Mi da il valore dell' operazione che mi devo mettere a fare
# # Mi dice anche poi in che verso mi devo mettere a fare
# def trimFirstLine(line):
# 	temp = line.split()
# 	boolean = False
# 	if temp[2] == b'a':
# 		boolean = True

# 	return boolean, temp[3][0:-1]

# # Prende una linea in formato 0 e 1 tutto attaccato, le divide e ritorna rappresentazioen ascii
# def binToStr(line):
# 	line = "0" + line
# 	n = 8
# 	listaBytes = ["0b" + line[i:i+n] for i in range(0, len(line), n)]
# 	answer = ''
# 	for binario in listaBytes:
# 		answer += chr(int(binario,2))
# 	return answer

# def strToBin(line):
# 	array =  [x for x in bytearray(js["message"], 'utf-8')]
# 	bytess = [format(x, 'b') for x in array]
# 	ans = ''
# 	for x in bytess:
# 		if len(x) < 8:
# 			x += "0" * (8 - len(x))
# 		ans += x
# 	if (ans[len(ans)-1] == '0'):
# 		ans = ans[0:-1]
# 	return ans


# # Prende la risposta, la trasforma in JSON e la manda al server
# def trimAndSend(line):
# 	dict= {"answer": line}
# 	js = bytes(str(json.dumps(dict) + '\n'), 'utf-8')
# 	conn.send(js)


# conn = remote("based.challs.olicyber.it", 10600)

# # Questi sono utili a mettere fuori gioco le linee iniziali
# conn.recvline()

# #Non printano niente
# i = 0;
# while(True):
	
# 	conn.recvline()	
# 	first = conn.recvline()

# 	if first != b'Ottimo!\n' and i > 1:
# 		print(first)
# 		break

# 	conn.recvline()

# 	# Le tre linee con le istruzioni
# 	firstline = conn.recvline()
# 	jsline = conn.recvline()
# 	# print(" io sono una linea di debug", jsline)
# 	secondline = conn.recvline()

# 	# Estrae l'operazione dalla linea
# 	andata, operation = trimFirstLine(firstline)

# 	js = json.loads(jsline)
# 	if operation == b'base64' and andata:	# testato funziona fino al print di debug
# 		message_bytes = js["message"].encode('ascii')
# 		base64_bytes = base64.b64encode(message_bytes)
# 		answer = base64_bytes.decode('ascii')
# 		trimAndSend(answer)
# 	elif operation == b'base64' and not andata: # testato funziona fino al print di debug
# 		message_bytes = js["message"].encode('ascii')
# 		base64_bytes = base64.b64decode(message_bytes)
# 		answer = base64_bytes.decode('ascii')
# 		trimAndSend(answer)
# 	elif operation == b'binari' and andata: # testato funziona fino al print di debug
# 		answer = strToBin(js["message"])
# 		trimAndSend(answer)
# 	elif operation == b'binario' and not andata: # Boh escono cose strane, con bytes non rappresentabili
# 		answer = binToStr(js["message"])
# 		trimAndSend(answer)

# 	elif operation == b'esadecimale' and andata: # testato funziona fino al print di debug
# 		answer = ''.join(hex(ord(x))[2:] for x in js["message"])
# 		trimAndSend(answer)
# 	elif operation == b'esadecimale' and not andata: # testato funziona fino al print di debug
# 		answer = ''.join([chr(int(''.join(c), 16)) for c in zip(js["message"][0::2],js["message"][1::2])])
# 		trimAndSend(answer)

# 	i += 1

# print(conn.recvline())
# print(conn.recvline())
# print(conn.recvline())


# print(conn.recvline())
# print(conn.recvline())
# print(conn.recvline())	