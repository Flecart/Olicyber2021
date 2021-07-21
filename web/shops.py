#! /usr/bin/env python3

import requests

# alla fine tutto questo non serviva, non so perch'e non prendesse la connessione
# comunque ho modificato i dati della richiesta con una intercettazione di burp e funziona

conn = requests.Session()

url = 'http://shops.challs.olicyber.it/buy.php'

prova = conn.post(url, data={"id":1,"cost":100})

print(prova.text)