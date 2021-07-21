#! /usr/bin/env python3

import requests
from base64 import b64encode, b64decode
from PIL import Image
from pytesseract import image_to_string
from bs4 import *

url = 'http://captcha.challs.olicyber.it'


conn = requests.Session()

res = conn.get(url)
soup = BeautifulSoup(res.text, 'lxml')

image_url = str(soup.find('img'))
src_index = image_url.find("src")
image_url = image_url[src_index+5:-3]
# print(soup.prettify())
print(image_url)

img = Image.open(requests.get(url + image_url, stream=True).raw)
ans = image_to_string(img)[:-2] # mette due acapo...
# print("-" + ans+"-")

for i in range(101):
    res = conn.post(url + '/next',data={'risposta': ans})
    soup = BeautifulSoup(res.text, 'lxml')
    print(soup.prettify())
    image_url = str(soup.find('img'))
    src_index = image_url.find("src")
    image_url = image_url[src_index+5:-3]
    # print(soup.prettify())
    print(image_url)

    img = Image.open(requests.get(url + image_url, stream=True).raw)
    ans = image_to_string(img)[:-2] # mette due acapo...

    print((str(i) +'-')*10)


#flag{https://xkcd.com/233/?vjc1GpKF}
