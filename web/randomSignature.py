#! /usr/bin/env python3.8
import requests
import time
import hashlib
from datetime import datetime
import random
import string
import hmac
# funzioni copiate da app.py
def get_random_string(length):
  letters = string.ascii_lowercase
  result_str = ''.join(random.choice(letters) for i in range(length))
  return result_str

def sign(text, key):
  textAsBytes = bytes(text, encoding='ascii')
  keyAsBytes  = bytes(key, encoding='ascii')
  signature = hmac.new(keyAsBytes, textAsBytes, hashlib.sha256)
  return signature.hexdigest()
# richiesta http al sito
url = 'http://trulyrandomsignature.challs.olicyber.it/'
res = requests.get(url)
biscotti = dict(res.cookies)

# mi ricreo la stringa di data giusta, con le info della richiesta
timeDiff = dict(res.headers)['X-Uptime']
uptime = int(datetime.utcnow().timestamp()-1 - int(timeDiff)) # -1 per mettere apposto latenza del sito credo
seed = datetime.fromtimestamp(uptime).strftime('%Y-%m-%d %H:%M:%S')
print(f"Seed: {seed}")
random.seed(seed)



SUPER_SECRET_KEY = get_random_string(32)
print(f"SUPER_SECRET_KEY: {SUPER_SECRET_KEY}")

# confronto la cifratura di not_admin ricavato cos`i e quella del sito
print(sign('admin', SUPER_SECRET_KEY))
print(sign('not_admin', SUPER_SECRET_KEY))
print(biscotti['signature'])
print()

# flag{m4yb3_1_5h0uld_h4v3_u53d_4_r34l_r4nd0m_5tr1ng}
# La cosa difficile qua `e stata riuscire ad affermare la differenza fra time.time() datetime.utcnow().timestamp()
# perch'e una prende UTC e laltra tempo locale...