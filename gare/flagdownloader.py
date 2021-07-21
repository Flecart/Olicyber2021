
import requests

import json

conn = requests.Session()
base_url = 'http://flagdownloader.challs.jeopardy.olicyber.it/download/flag/'
current = '0'
flag = ''
while True:
    
    res = conn.get(base_url + current)
    current = json.loads(res.text)['n']
    flag += json.loads(res.text)['c']
    print(flag)
    print(res.text)

# flag{la_pazienza_e_la_virtu_dei_forti_3578735382}
