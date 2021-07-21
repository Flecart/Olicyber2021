#! /bin/python3

# import base64

# # base64_string = "LyJ39APQedoOlAD3O+dIDVhUSmzG0NTlp2UvfUVeoZetNtGUI8RIyE3V59OMsw=="
# # base64_bytes = base64_string.encode("ascii")
  
# # sample_string_bytes = base64.b64decode(base64_bytes)
# # sample_string = sample_string_bytes.decode("ascii")
  
# # print(f"Decoded string: {sample_string}")


import requests
from bs4 import BeautifulSoup

url = "http://infinite.challs.olicyber.it/"


session = requests.Session()
response = session.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
# print(response.content)
operator = str(soup.find("h2")).split()[1]
content = str(soup.find("p")).split()
print(operator)
print(content)
j = 0
while(True):
	# if i % 10 == 0:
	# 	print("siamo arrivati alla numero:",i)
	if operator == "GRAMMAR":
		# LyJ39APQedoOlAD3O+dIDVhUSmzG0NTloWU6MgQf8dTvZYSQP5UFjR21sYaM
		# letter=1&submit=Submit
		lettera = content[2][1]
		parola = content[-2][1:-2]
		i = 0
		for x in parola:
			if lettera == x:
				i += 1
		res = session.post(url, data={"letter": i})
		soup = BeautifulSoup(res.content, 'html.parser')
		# print(soup)
		# print("sto debuggando lettera e parola", lettera,parola)
	elif operator == "MATH":
		# sum=664
		a = int(content[3])
		b = int(content[5][0:-1])
		res = session.post(url, data={"sum": a+b})
		soup = BeautifulSoup(res.content, 'html.parser')
		# print(soup)

		# print("sto debuggando a e b", a,b)
	elif operator == "ART":
		# Verde=
		colore = content[-2][0:-1]
		res = session.post(url, data={f"{colore}": ""})
		soup = BeautifulSoup(res.content, 'html.parser')
		# print(soup)
		# print(colore)
	else:
		print(soup)

	operator = str(soup.find("h2")).split()[1]
	content = str(soup.find("p")).split()
	print(j, operator, " :: ", " ".join(content[1:-1]))

	j += 1