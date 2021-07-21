#!/bin/env python3

from pwn import *
import requests
import attacklib
import targetstorage
import sys
import json

service_name = None
script_name = sys.argv[0]
headers = attacklib.getHeadersWithRandomUserAgent()

ip = sys.argv[1]

if service_name:
	attacksjson = json.loads(requests.get("https://scoreboard.ctf.saarland/attack.json").text)
	getid = attacksjson['flag_ids'][service_name][ip]

storage = targetstorage.TargetStorage(script_name, ip, attack_dir="/tmp/attacklib", base64_encoded=True