#! /usr/bin/env python3 



b = bytes.fromhex('6ce7bd516307514ea338264b076265ec')
c = bytes.fromhex('0a8bdc361826647dc04a153f580b1391')
# a021769cb28cced76ae0bf95f2a1b93b
# 6ce7bd516307514ea338264b076265ec



# e07555de84b97f51968e708a017556a2
# 45c4db4fc76c473b37f5e21384a70dfc
# 89aacd21ffd10487f7b2a4fd455dd6b8
ans = []
for x in range(16):
    char = hex(c[x] ^ b[x])[2:]
    if len(char) == 1:
        char = "0" + char
    ans.append(char)

print("".join(ans))