#! /bin/python3

with open("dopp.jpg", "rb") as f:
	byte = f.read()
	# set up for cycle to extract bytes

	index = 0
	while index < len(byte):
		currentBytes = byte[index:index+3]

		nextIndex = byte[(index+3):].find(currentBytes)
		if (nextIndex == -1):
			print("Voglio uscire, fino a ora ho raggiunto l' index", index)
			exit(0)

		#metto apposto l' index 
		nextIndex += 3 +index
		with open("final",'ab') as appends:
			appends.write(byte[index:nextIndex])
			appends.close()

		index += 2*(nextIndex -index)
		print(nextIndex)
		print(index)
		print(hex(byte[nextIndex]))

print("esco invece in altro modo e sono felice lo stesso")