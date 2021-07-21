#! /bin/python3


import dns.resolver

directions = ["up", "down", "right", "left"]
knowPlace = ["00000000-0000-4000-0000-000000000000.maze.localhost"]

def parseAns(answer):
	return "".join([str(ans)[0:-1] for ans in answer])

def checkTXT(domain):
	answer = resolver.resolve(domain, "TXT")
	message = parseAns(answer)
	boolean = len(message) > 0
	return boolean

# in pratica `e la stessa della precedente, ma questo invece printa la risposta txt
def printAns(domain):
	answer = resolver.resolve(domain, "TXT")
	message = parseAns(answer)
	print("Ho trovato una risposta txt in", domain)
	print(message)

def cercatore(domain, moves=[]):
	temp = moves
	for dirs in directions:
		moves = temp
		try:
			answer = resolver.resolve(dirs + "." + domain, "CNAME")
		except:
			print("Sono in", domain, "non ho trovato niente muovendomi verso", dirs)
			continue
		else:
			newDomain =  parseAns(answer)
			# se ho gia visitato questo punto non ci andare ancora
			if newDomain in knowPlace:
				continue
			else:
				knowPlace.append(newDomain)
			areTXT = checkTXT(newDomain)
			if areTXT:
				printAns(newDomain)
				print("La sequenza esatta di mosse is", moves)
				exit(0)
			else:
				moves.append(dirs)
				cercatore(newDomain, moves)


resolver = dns.resolver.Resolver()
resolver.nameservers=["65.21.60.158"]  # 65.21.60.158
resolver.port = 10500

# 1eb650c2-0bb3-4513-af02-120685339b9a.maze.localhost INDIRIZZO FINALE
# Sotto la seguenza esatta di mosse per raggiungere la destinazione ahah
# ['down', 'down', 'right', 'up', 'right', 'down', 'right', 'down', 'down', 'down', 'left', 'right', 'right', 'left', 'up', 'down', 'left', 'right', 'right', 'up', 'left', 'down', 'down', 'down', 'right', 'right', 'up', 'down', 'right', 'left', 'up', 'left', 'down', 'down', 'right', 'left', 'up', 'down', 'down', 'down', 'right', 'down', 'down', 'right', 'up', 'left', 'up', 'right', 'left', 'down', 'right', 'left', 'left', 'up', 'down', 'down', 'down', 'down', 'right', 'up', 'right', 'left', 'down', 'down', 'left', 'up', 'right', 'down', 'right', 'left', 'left', 'left', 'left', 'up', 'up', 'up', 'left', 'down', 'down', 'right', 'left', 'down', 'left', 'right', 'up', 'up', 'up', 'right', 'left', 'left', 'up', 'left', 'up', 'up', 'left', 'left', 'down', 'down', 'right', 'right', 'up', 'down', 'right', 'left', 'up', 'left', 'left', 'up', 'right', 'left', 'down', 'left', 'left', 'down', 'left', 'right', 'up', 'right', 'up', 'left', 'left', 'down', 'left', 'down', 'left', 'up', 'right', 'down', 'right', 'left', 'left', 'down', 'down', 'down', 'left', 'down', 'down', 'down', 'left', 'up', 'left', 'left', 'down', 'left', 'up', 'left', 'left', 'left', 'up', 'left', 'up', 'right', 'left', 'down', 'down', 'down', 'right', 'left', 'left', 'up', 'up']


cercatore(knowPlace[0])

