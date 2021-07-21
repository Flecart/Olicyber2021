#! /usr/bin/env python3

from hashlib import md5
import string 

digits = list(string.digits)
i = 0

def isNumber(string):
	for x in string:
		if x not in digits:
			return False
	return True


while True:
	result = md5(str(i).encode()).digest().hex()
	payload = '0e' + str(i)
	print(payload,result)
	# if (str(i) == result[:len(str(i))]) and result[len(str(i))] == 'e':
	# 	print('trovato',i,result)
	# 	break

	if result[:2] == '0e' and isNumber(result[2:24]):
		if i % 1000
		print('trovato',payload,result)
		break
	i+= 1

 # flag{0mg_php_c0mp4r150n_r34lly_5uck5}

# ho provato a farlo con python ma a quanto pare il md5 e leggermente diverso, non so perch'
# equindi ho usato questo script in php e funziona, ho trovato un numero, interpretato con 0equalcosa (entrambi uguali a0)
# e simili...

# QUi sotto lo script buono in php
# <?php 
# // echo substr(md5('0e1789525'), 0, 24);

# $i = 0;
# $stringa = "0e" . (string)$i;
# echo $stringa;

# while (true) {
# 	$payload = "0e" . (string)$i;
# 	$md = md5($payload);
# 	echo "$payload $md'\n'";
# 	if ($payload == substr($md,0,24)) {
# 		echo "ho trovato qualcosa $payload $md .'\n'";
# 		break;
# 	}
	
# 	$i++;
# }
# // 0e2977606 0e80421617475399026384016f8d4ad2