#! /usr/bin/env python3 

n = 9565158649535229609530047362785645907094563351070470563788237
b = 2771826449193354891007108898387
c = 3450850486082503930213321971551

e = 65537
phi = (b-1) * (c-1)


d = pow(e,-1,phi)

c1 = 6513402340379073542230710001434049959082564276254477896792619
c2=2739603094136133383923409703861575117091198809308633380325460


p1 = pow(c1,d,n)
p2 = pow(c2,d,n)

print(p1)
print(p2)

p1 = hex(p1)[2:]
p2= hex(p2)[2:]

ans = p1+p2

print(ans)

# flag{s0m3tim3s_s1z3_d0es_m4tt3r}