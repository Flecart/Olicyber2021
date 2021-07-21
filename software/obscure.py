#! /usr/bin/env python3

# gestione output di file compilato da me per prove
# from Crypto.Util.number import long_to_bytes
# import subprocess

# stringa = 'you-spin-my-head-right-round-right-round'
# payload = f'./obs {stringa} {len(stringa)}' 
# print(payload)

# subprocess = subprocess.Popen(payload, shell=True, stdout=subprocess.PIPE)
# out = subprocess.stdout.readline().strip()
# hex = subprocess.stdout.readline().strip()
# # veryOut = subprocess.stdout.read()
# print(out)
# print(hex)
# hex = hex.split(b' ') # divido per ogni char
# byte_string = [int(i.decode()[2:],16) & 0xff for i in hex]
# print(byte_string)




xor_this = [0xbe, 0xc0, 0xc9, 0x76, 0xf5, 0xab, 0xf6, 0x09, 0x56, 0x19, 0x85, 0xfd, 0xe1, 0x4d, 0x0e, 0x83, 0xe3, 0x46, 0xa8, 0xa6, 0x5b, 0xcb, 0x7c, 0x8b, 0xbe, 0x33, 0x1c, 0x24, 0x74, 0x51, 0xb3, 0x1b, 0xcb, 0xca, 0x8f, 0xec, 0x98, 0xbf, 0x78, 0x5b]

def xor(a,b):
    return bytes([x ^ y for x,y in zip(a,b)])

def swap_2(array):
    ans = [0]*len(array)
    for i in range(0,len(array),2):
        ans[i] = array[i+1]
        ans[i+1] = array[i]

    return ans
def encrypt_position(array):
    ans = [0] * len(array)
    for i in range(len(array)):
        ans[i] = chr(array[i] + i)

    return "".join(ans)

def substitute(arr, char, what):
    arr = list(arr)
    for i in range(len(arr)):
        if arr[i] == char: arr[i] = what
    return "".join(arr)

target = bytes.fromhex('e78e9a5cbae0b54e735dcadfdd753db6fe079f926ff46bb0890f280d65649833e3f984c3b38f5046')
target = swap_2(target)

xor_this = swap_2(xor_this)
target = xor(xor_this, target)
target = swap_2(target)
target = encrypt_position(target)
target = target.lower()
target = substitute(target, chr(0x40),chr(0x7a))
target = substitute(target, chr(0x2d),chr(0x5f))
target = substitute(target, chr(0x69),chr(0x21))
target = substitute(target, chr(0x74),chr(0x37))
target = substitute(target, chr(0x40),chr(0x7a))
target = substitute(target, chr(0x6f),chr(0x30))
target = substitute(target, chr(0x65),chr(0x33))
target = substitute(target, chr(0x61),chr(0x34))
target = substitute(target, 's','$')
print('flag{%s}' % target, type(target))
# out = xor(xor_this, byte_string)
# print(out, len(out))
# 
# leet boy
print("(%s, %s) ,(%s, %s),(%s, %s),(%s, %s),(%s, %s),(%s, %s),(%s, %s),(%s, %s)" %(chr(0x5f),chr(0x2d),chr(0x21),chr(0x69),chr(0x37),chr(0x74),chr(0x7a),chr(0x40),chr(0x30),chr(0x6f),chr(0x33),chr(0x65),chr(0x34),chr(0x61),chr(0x24),chr(0x4f)))
#   local_18[0] = 0x7a;
#   local_18[1] = 0x40;

# flag{y0u_$p!n_my_h34d_r!gh7_r0und_r!gh7_r0und} 

# region tentativo angr fallitooo
# import angr
# import claripy
# base_address = 0x00100000

# success_address = 0x00101e74
# failure_address = 0x00101e8a
# proj = angr.Project('./ObscureSecurity', main_opts={'base_addr': 0})

# arg = claripy.BVS('arg', 8*0x20)

# state = proj.factory.entry_state(args=['./ObscureSecurity', arg])
# simgr = proj.factory.simulation_manager(state)
# simgr.explore(find=success_address, avoid=failure_address)
# print("len(simgr.found) = {}".format(len(simgr.found)))

# if len(simgr.found) > 0:
#     s = simgr.found[0]
#     print("argv[1] = {!r}".format(s.solver.eval(arg, cast_to=bytes)))
# endregion

#region una copiatrura online
# https://crackmes.one/crackme/5df26b4033c5d419aa013362

# import angr
# import claripy
# import subprocess
# import sys


# def get_arg():
#     n = int(sys.argv[1])
#     if n > 0 and n < 1000:
#         return n
#     else:
#         print("usage:\t./glowwine_keygen.py < number of keys to compute (0 - 999) >")

# def solve():
#     num_keys = get_arg()
#     base_address = 0x00100000

#     success_address = 0x00101e6c
#     failure_address = 0x00101e8a
#     proj = angr.Project("ObscureSecurity",
#                         main_opts = {"base_addr": base_address}, # PIE binary
#                         auto_load_libs = False)

#     # create an array of bitvectors so that the value of each can easily be
#     # constrained to the range of printable ASCII characters
#     key_bytes = [claripy.BVS("byte_%d" % i, 8) for i in range(5)]
#     key_bytes_AST = claripy.Concat(*key_bytes)

#     # we want to generate valid keys, so a symbolic variable is passed to 
#     # the state rather than a concrete value
#     state = proj.factory.entry_state(args = ["ObscureSecurity", key_bytes_AST])

#     # impose constraints on bitvectors the symbolic key is composed of
#     for byte in key_bytes:
#         state.solver.add(byte >= 0x21, byte <= 0x7e)

#     sim_mgr = proj.factory.simulation_manager(state)

#     # find path to message indicating key was correct
#     sim_mgr.explore(find = success_address, avoid = failure_address)

#     # generate keys
#     if len(sim_mgr.found) > 0:
#         found = sim_mgr.found[0]
#         keys = found.solver.eval_upto(key_bytes_AST, num_keys, cast_to = bytes)

#         # check keys
#         for key in keys:
#             output = subprocess.run(["./ObscureSecurity", key], stdout = subprocess.PIPE)
#             print("[ + ]  %s\t%s" % (key.decode("ascii"), repr(output.stdout)))
#     else:
#         print("[ x ] No solution found")

# solve()
#endregion

# region cose copiate fallite
# base_address = 0x00000000

# success_address = 0X00101e6c
# failure_address = 0x00101384

# flag_length = 41

# project = angr.Project('./ObscureSecurity',main_opts = {"base_addr": base_address})

# flag_chars = [claripy.BVS('flag_%i' %i, 8) for i in range(flag_length)]
# flag = claripy.Concat( *flag_chars )

# state = project.factory.full_init_state(
#     args = ['./ObscureSecurity', flag],
#     add_options = angr.options.unicorn
# )

# for k in flag_chars:
#     state.solver.add(k >= ord('!'))
#     state.solver.add(k <= ord('-'))

# sim_manager = project.factory.simulation_manager(state)
# sim_manager.explore(find = success_address, avoid = failure_address)

# if (len(sim_manager.found) > 0):
#     for found in sim_manager.found:
#         print(found.posix.dumps(0))

# endregion 