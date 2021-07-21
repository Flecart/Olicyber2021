#! /usr/bin/env python3

# capisco dall'assembly che questo va a comparare sti due in questo modo
# quindi copio i valori e mi ricavo la chiave
# avrei potuto non fare bruteforce ma cosi e pi`u semplice dai
compareTo = bytes.fromhex('bdc3b5acd5d9cddbb5b7c9e8b5bd81c7d689c4dbbc77ddd4')

shift = bytes.fromhex('575754455a66586842425776545050686a55657550437657')

from string import printable

print(printable)
print(len(shift))
flag = ''
for i in range(24):
    for x in printable:
        if (ord(x) + shift[i] - compareTo[i]) == 0: # per comparare fa proprio questo
            flag += x
            break

print(flag)
# flag{sussurram1_l4_fl4g}