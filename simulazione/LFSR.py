#! /usr/bin/env python3
import random
from Crypto.Util.number import bytes_to_long
# region classe LFSR usato per criptare
def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

class LFSR(object):
    def __init__(self, s):
        self.s = list(map(int, s))

    def gen_stream(self, n):
        out = []
        for i in range(n):
            out.append(self.s[0]^self.s[12]^self.s[21]^self.s[30]^self.s[50])
            self.s = self.s[1:] + [self.s[0]^self.s[3]^self.s[7]^self.s[9]]
        return out


# initial_state = random.randint(0,2**56) # 2**56 = 72057594037927936, impossible to bruteforce!
# initial_state = [int(x) for x in bin(initial_state)[2:].rjust(56, '0')]
# L = LFSR(initial_state)

# k = b""

# for i in range(len(flag)):
#     k += bytes([int("".join(str(x) for x in L.gen_stream(8)), 2)])


# print(xor(flag, k).hex())

# endregion

# estrazione bit noti, da data.txt
ciph = bytes.fromhex('2a9ea39adb1c4784b565df976fa7fc34ca5bddbb4d35c597c13f53ee8f4da0c24b5378cec24460a1bf3df5b021')
known = xor(ciph[:5], b"flag{")
bit_out = [int(x) for x in bin(bytes_to_long(known))[2:].rjust(40, '0')] # trasformo da bytestring a bit array


# creazione secondo LFSR pi`u semplice
# non capisco perch'e funziona
class LFSR2(object):
    def __init__(self, s):
        self.s = list(map(int, s))

    def gen_stream(self, n):
        out = []
        for i in range(n):
            out.append(self.s[0])
            self.s = self.s[1:] + [self.s[0]^self.s[3]^self.s[7]^self.s[9]]
        return out

# exploit di bruteforce, pochi casi possibili
for j in range(2**16):

    # creo stato iniziale utile
    temp = bit_out + [int(x) for x in bin(j)[2:].rjust(16, '0')]
    L = LFSR2(temp)
    k = b""
    for i in range(len(ciph)):
        k += bytes([int("".join(str(x) for x in L.gen_stream(8)), 2)])
    flag = xor(ciph,k)


    # condizione di uscita, stranamente esce...
    if  "\\x" not in str(flag):
        print(flag, len(flag))
        # break

    # conto
    if j %1000 == 0:
        print(' sono arrivato a ',j)


    # flag{6u355_wh47?_l1n34r_func710n5_4r3_l1n34r}