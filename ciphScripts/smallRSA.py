#! /usr/bin/env python3

n= 121188535871798118811428322495136173485838157702837603009744079502828661170574654643712519826693731103670617468427120197687519224611728159372629028899279680740201176466228593180097000630667826923128885153190352359299571456927587933797154384731664367396394374086703053646510220882981791309024543386831488440013
e= 3
ct=56274920108133183710879347789095782313165243853788407193317419375243717146801757114129876005705242550492379484281774120724787040219649340446091878053221949541
# flag{meglio_usare_tutta_la_flag} per hashes
# flag{usa_e_piu_grandi}
from utilities import * # mi faccio le due funzioni che mi servono per avere la falg

decoded = nth_root(ct,e)
stringa = hexToStr(hex(decoded)[2:])

print(stringa)

# p = []

# for x in range(len(c)):
# 	decoded = nth_root(c[x],e)
# 	if decoded ** 
# 	stringa = hexToStr(hex()[2:])
# 	p.append(stringa)
