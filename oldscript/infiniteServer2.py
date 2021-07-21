#! /bin/python3

import requests
from bs4 import BeautifulSoup
 
session  = requests.Session()

url = "http://infinite.challs.olicyber.it/"

res = session.get(url)

res = res.text

# print(res)
# 1 in qualcosa per vedere se `e veramente dentro
# 2 cerca la stringa con find
# 3 beautfiulsoup
# Parse the html content

soup = BeautifulSoup(res, "lxml") # O REGEX

while True:
	if "MATH TEST" in res:
		print("ho trovato un test di")
		paragraph = soup.find("p")

		arr = str(paragraph).split(" ")
		addendo = arr[3]
		addendo2 = arr[5][:-1] 
		print(addendo, addendo2)
		ans = int(addendo2) + int(addendo)
		print(ans)
		res = session.post(url, data={"sum": ans})
		
		# print(res.text)

	elif "ART TEST" in res:
		# print("ARTEEE")
		paragraph = str(soup.find("p"))

		if "Blu" in paragraph:
			# print(" bluuu ")
			res = session.post(url, data={"Blu": ""})
		elif "Verde" in paragraph:
			# print( " verde ")
			res = session.post(url, data={"Verde": ""})
		elif "Rosso" in paragraph:
			# print( " rosso ")
			res = session.post(url, data={"Rosso": ""})

		# print(res.text)

	elif "GRAMMAR TEST" in res:
		print("grammar!")
		paragraph = soup.find("p")

		arr = str(paragraph).split(" ")
		lettera = arr[2][1]
		parola = arr[-2][1:-2]
		i = 0
		for x in parola:
			if lettera == x:
				i += 1

		ans = i

		res = session.post(url, data={"letter": ans, "submit": "Submit"})
	# print(res.text)
	res = res.text
	soup = BeautifulSoup(res, "lxml")

	print(soup)
print(paragraph)


# 1 COSA CI RICHIEDE !!!!!!!!!!!!!!!!!!RIUSCITO
# 2 CALCOLARE LA RISspOTA RIUSCITO

# 3 SUBMITTARE LA RISPOSTA 
# 4 RICEVERE ALTRE RISPOSTE