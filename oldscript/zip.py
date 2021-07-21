#! /usr/bin/env python3

import zipfile
from tqdm import tqdm

# the password list path you want to use, must be available in the current directory
wordlist = "worlist.txt"
# the zip file you want to crack its password


for i in reversed(range(101)):
	zip_file = f"{i}.zip"

	# initialize the Zip File object
	zip_file = zipfile.ZipFile(zip_file)
	# count the number of words in this wordlist
	# print the total number of passwords
	wordlist = "worlist.txt"
	with open(wordlist, "rb") as wordlist:
	    for word in tqdm(wordlist, total=1000000, unit="word"):
	        try:
	            zip_file.extractall(pwd=word.strip())
	        except:
	            continue
	        else:
	            print("[+] Password found:", word.decode().strip())
	            break
        