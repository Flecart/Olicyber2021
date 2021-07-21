#! /usr/bin/env python3


# flag{rsa_Rsa_rSa_rsA_rsa_crt_ftw}
n = []
c = []
with open('chinese.txt','r') as f:
	for x in range(17):
		mod = int(f.readline().split()[-1])
		ciphertext = int(f.readline().split()[-1])
		n.append(mod)
		c.append(ciphertext)

	e = int(f.readline().split()[-1])
	
bigNumber = 1
for x in n:
	bigNumber*=x
def calcoloAddendoCinese(index):
	moltiplicazione = 1
	for i in range(17):
		if i!=index:
			moltiplicazione *= n[i]
	inversoMoltiplicativo = pow(moltiplicazione,-1,n[index])

	return c[index]*moltiplicazione*inversoMoltiplicativo

# funzione radice perfetta importata da
# https://riptutorial.com/python/example/8751/computing-large-integer-roots
def nth_root(x, n):
    # Start with some reasonable bounds around the nth root.
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1

    
soluzione = 0
for x in range(17):
	soluzione += calcoloAddendoCinese(x)

soluzione = pow(soluzione,1,bigNumber) # modulo veloce
plaintext = nth_root(soluzione,17)
print(plaintext)
if plaintext**17 == soluzione:
	print("evviva")
	string = hex(plaintext)[2:]
	res = b""
	for i in range(0, len(string), 2):
		c = string[i:i+2]
		try:
			res += bytes.fromhex(c)
		except:
			continue

	print(res)

# Controllo a vedere se gli n sono fra loro tutti primi, perch'e se `e cosei allora
# avrei trovato i p generatori senza nessuna difficolt`a

# from Crypto.Util.number import GCD

# for x in range(17):
# 	i = 0
# 	while i < 17:
# 		if i == x:
# 			i+=1
# 			continue
# 		else:
# 			print(f"GCD fra {x} e {i} e'",GCD(n[x],n[i]))
# 			i+=1
# 	print("numero successivo", x+1)