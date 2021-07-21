#! /usr/bin/env python3

# questo `e la seconda versione di questo script
from pwn import remote
import time

conn = remote('time.challs.olicyber.it', 10505)
conn.recv()
times = []

n = 200
rilevations = 5

def get_bit(index):
    global conn
    try:
        conn.recv()
        conn.sendline('1')
        conn.sendline(str(index))

        computation_time = time.time()
        conn.recv()
        a = conn.recvline()     
        computation_time = time.time() - computation_time

        if ":(" in a.decode().strip():
            return None

        return computation_time
    except EOFError:
        conn = remote('time.challs.olicyber.it', 10505)
        conn.recv()
        return -1

def get_bits() -> None:
    temp = []
    i = 0
    for i in range(0, n):
        t = get_bit(i)
        while t == -1 or not t:
            t = get_bit(i)            

        temp.append(t)
        i += 1
    times.append(temp) 

print("[*] Flag lenght:", n)

for i in range(0, rilevations):
    print("[*] " + str(i+1) + "° rilevation")
    get_bits()

avg = 0
for i in range(0, rilevations):
    tmp = times[i]
    tmp.sort()
    tmp = tmp[1:-1]
    avg += sum(tmp) / len(tmp)
avg = avg / rilevations
print("avg:", avg)

flag = ""
#avg of index
for j in range(0, n):
    avg_bit = 0
    for i in range(0, rilevations):
        avg_bit += times[i][j]
    avg_bit = avg_bit / rilevations

    if avg_bit > avg:
        flag += "1"
    else:
        flag += "0"

print(flag)
flag = bytes.fromhex(hex(int(flag, 2))[2:])
print(flag)

# import time
# from pwn import *
# conn = remote('time.challs.olicyber.it',10505)
# answer = ''

# start = time.time()
# for i in range(20):
# 	conn.recvuntil('> ')
# 	conn.sendline('1')
# 	conn.recvuntil('vuoi ricevere? ')
# 	conn.sendline(str(1))

# finish = time.time()

# print(finish - start)
# print((finish - start)/200)