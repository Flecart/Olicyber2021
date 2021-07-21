#!/usr/bin/env python3

# import os
# import random
# import signal
# from Crypto.Cipher import AES

# TIMEOUT = 300

# assert("FLAG" in os.environ)
# flag = os.environ["FLAG"]
# key = os.environ["KEY"]
# assert(len(key) == 16)
# assert(flag.startswith("flag{"))
# assert(flag.endswith("}"))


# def encrypt_flag():
#     iv = os.urandom(16)

#     cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
#     encrypted = cipher.encrypt(flag.encode())
#     ciphertext = iv.hex() + encrypted.hex()

#     return ciphertext

# def decrypt(ciphertext):
#     ciphertext = bytes.fromhex(ciphertext)

#     cipher = AES.new(key.encode(), AES.MODE_ECB)
#     try:
#         decrypted = cipher.decrypt(ciphertext)
#     except ValueError as e:
#         return str(e)

#     return decrypted.hex()

# def handle():
#     ct = input('ciphertext: ')
#     print(decrypt(ct))


# if __name__ == "__main__":
#     signal.alarm(TIMEOUT)
#     handle()


# ans = []
# for x in range(16):
#     ans.append(a[x] ^ b[x])

# print(ans)
# a = [197, 79, 247, 195, 22, 235, 181, 187, 216, 88, 168, 187, 43, 60, 227, 164]
# b = [76, 30, 156, 139, 142, 179, 104, 95, 85, 71, 20, 123, 125, 14, 105, 35]


# ans = ""
# for x in b:
#     h = hex(x)[2:]
#     print(h)
#     if len(h) == 1:
#         h = "0" + h
#     ans += hex(x)[2:]
# c54ff7c316ebb5bbd858a8bb2b3ce3a44c1e9c8b8eb3685f5547147b7d0e6923
# print(ans)
# 744b533031f4e57b3d7a789b81d48420

# 866bb5802051d56f37b1073a501b4afe
# 4324424336ba60d4efe9af817b27a95a
# 0f3adec8b809088bbaaebbfa0629c079


a = bytes.fromhex('866bb5802051d56f37b1073a501b4afe')


b = bytes.fromhex('4324424336ba60d4efe9af817b27a95a')
# b = bytes.fromhex('e007d4e75b0ea60068c8684f0f702491')
c = bytes.fromhex('347b2a2c41e52396acb6d8ee094cda27')
ans = []
for x in range(16):
    char = hex(c[x] ^ b[x])[2:]
    if len(char) == 1:
        char = "0" + char
    ans.append(char)

print("".join(ans))

# ans = []
# for x in range(16):

#     char = hex(a[x] ^ b[x])[2:]
#     if len(char) == 1:
#         char = "0" + char
#     ans.append(char)

# print("".join(ans))

# c54ff7c316ebb5bbd858a8bb2b3ce3a44c1e9c8b8eb3685f5547147b7deo6923


# 4c1e9c8b8eb3685f5547147b7d0e6923c54ff7c316ebb5bbd858a8bb2b3ce3a4

# 710e0dd6208d0673f7063158b681f8cf