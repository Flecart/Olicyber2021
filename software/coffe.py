#! /usr/bin/env python3


h = '630:624:622:612:609:624:623:610:624:624:567:631:638:639:658:593:546:605:607:585:648:636:635:704:702:687:687:682:629:699:633:639:634:637:578:622:620:617:606:615:568:633:589:587:645:639:653:654:633:634'

hash_numbers = h.split(':')
hash_numbers = [int(x) for x in hash_numbers]

#WRITEUP
# 1. il primo passo e quello di calcolare le varie differenze dalla char numero uno
#   dopo aver fatto questo sarebbe facile bruteforcare e cercare una striga che funzionasse
#   infatti si vede nel codice della prima regione creare un array con le differenze

# 2. il secondo passo e cercare quale funzioni
# FLAG: flag{jav4_4nd_l1n3ar_3qu4t10ns_sh0uld_n3v3r_b3_t0gh3t3r}

# region mi calcolo array delle differenze
differences = [0] * 50
flag_len = 50

lastDiff = hash_numbers[0] - hash_numbers[1]
differences[7] = lastDiff
index = 7

# loop che mi prende offset dal primo char di tutti e 50
while index != 0:
    lastDiff = lastDiff + hash_numbers[index] - hash_numbers[(index + 1) % flag_len]
    index = (index + 7) % flag_len
    differences[index] = lastDiff

print(differences)
#endregion

# region provo a guardare le differenze che ho trovato
diffArray = [0, 9, -12, 54, 11, 54, -4, 6, 11, -2, 57, -4, 55, 9, -8, 11, 55, -7, -11, 54, -10, 57, 58, -4, -9, 11, -9, 2, 58, -11, -2, 6, 11, -4, 55, -12, 55, -8, 11, 8, 55, 11, -10, 58, 3, 2, 55, -10, 55, -8]

cosoArray = []
for begin in range(32,127):
    isPossible = True
    currentString = ''
    for diff in diffArray:
        valoreChar = begin - diff

        # se una char non `e printabile allora dico che non `e possibile
        if valoreChar < 32 or valoreChar > 127:
            print('Nessun valore possibile per i =', begin)
            isPossible = False
            break
        currentString += chr(valoreChar)

    if isPossible:
        print(currentString)
        cosoArray.append(currentString)

print(cosoArray)
# endregion

# questa parte di codice e solo perch'e sono orbo e non trovavo la flag prima
# region provo a debuggare qualcosa
# output = ['ZQf$O$^TO\\!^#QbO#ae$d! ^cOcX e\\TO^#f#bOR#Od WX#d#b', '[Rg%P%_UP]"_$RcP$bf%e"!_dPdY!f]UP_$g$cPS$Pe!XY$e$c', '\\Sh&Q&`VQ^#`%SdQ%cg&f#"`eQeZ"g^VQ`%h%dQT%Qf"YZ%f%d', "]Ti'R'aWR_$a&TeR&dh'g$#afRf[#h_WRa&i&eRU&Rg#Z[&g&e", "^Uj(S(bXS`%b'UfS'ei(h%$bgSg\\$i`XSb'j'fSV'Sh$[\\'h'f", '_Vk)T)cYTa&c(VgT(fj)i&%chTh]%jaYTc(k(gTW(Ti%\\](i(g', "`Wl*U*dZUb'd)WhU)gk*j'&diUi^&kbZUd)l)hUX)Uj&]^)j)h", "aXm+V+e[Vc(e*XiV*hl+k('ejVj_'lc[Ve*m*iVY*Vk'^_*k*i", 'bYn,W,f\\Wd)f+YjW+im,l)(fkWk`(md\\Wf+n+jWZ+Wl(_`+l+j', 'cZo-X-g]Xe*g,ZkX,jn-m*)glXla)ne]Xg,o,kX[,Xm)`a,m,k', 'd[p.Y.h^Yf+h-[lY-ko.n+*hmYmb*of^Yh-p-lY\\-Yn*ab-n-l', 'e\\q/Z/i_Zg,i.\\mZ.lp/o,+inZnc+pg_Zi.q.mZ].Zo+bc.o.m', 'f]r0[0j`[h-j/]n[/mq0p-,jo[od,qh`[j/r/n[^/[p,cd/p/n', 'g^s1\\1ka\\i.k0^o\\0nr1q.-kp\\pe-ria\\k0s0o\\_0\\q-de0q0o', 'h_t2]2lb]j/l1_p]1os2r/.lq]qf.sjb]l1t1p]`1]r.ef1r1p', 'i`u3^3mc^k0m2`q^2pt3s0/mr^rg/tkc^m2u2q^a2^s/fg2s2q', 'jav4_4nd_l1n3ar_3qu4t10ns_sh0uld_n3v3r_b3_t0gh3t3r', 'kbw5`5oe`m2o4bs`4rv5u21ot`ti1vme`o4w4s`c4`u1hi4u4s', 'lcx6a6pfan3p5cta5sw6v32puauj2wnfap5x5tad5av2ij5v5t', 'mdy7b7qgbo4q6dub6tx7w43qvbvk3xogbq6y6ube6bw3jk6w6u', 'nez8c8rhcp5r7evc7uy8x54rwcwl4yphcr7z7vcf7cx4kl7x7v', 'of{9d9sidq6s8fwd8vz9y65sxdxm5zqids8{8wdg8dy5lm8y8w', 'pg|:e:tjer7t9gxe9w{:z76tyeyn6{rjet9|9xeh9ez6mn9z9x', 'qh};f;ukfs8u:hyf:x|;{87uzfzo7|skfu:}:yfi:f{7no:{:y', 'ri~<g<vlgt9v;izg;y}<|98v{g{p8}tlgv;~;zgj;g|8op;|;z', 'sj\x7f=h=wmhu:w<j{h<z~=}:9w|h|q9~umhw<\x7f<{hk<h}9pq<}<{']

# for stringa in output:
#     exit = ''
#     for i in range(50):
#         n = 0
#         for j in range(7):
#             n += ord(stringa[(i + j) % 50])
#         if len(exit) == 0: exit = str(n)
#         else: exit += ":" + str(n)
#     print(exit)
#     if exit[:3] == "630": print(stringa)
# endregion

# DISASSEMBLED JAVA CODE
# /*
#  * Decompiled with CFR 0.150.
#  */
# import java.io.Serializable;

# public class coffe {
#     static String hash = "630:624:622:612:609:624:623:610:624:624:567:631:638:639:658:593:546:605:607:585:648:636:635:704:702:687:687:682:629:699:633:639:634:637:578:622:620:617:606:615:568:633:589:587:645:639:653:654:633:634";

#     public static void main(String ... arrstring) {
#         if (arrstring.length != 1) {
#             System.out.println("Usage: java Challenge <password>");
#             System.exit(1);
#         }
#         if (coffee_hash.checkPassword(arrstring[0])) {
#             System.out.printf("flag{%s}\n", arrstring[0]);
#         } else {
#             System.out.println("Incorrect password!");
#         }
#     }

#     public static boolean checkPassword(String string) {
#         Object object = "";
#         for (int i = 0; i < string.length(); ++i) {
#             int n = 0;
#             for (int j = 0; j < 7; ++j) {
#                 n += string.charAt((i + j) % string.length());
#             }
#             object = (String)object + (Serializable)(((String)object).length() == 0 ? Integer.valueOf(n) : ":" + n);
#         }
#         return hash.equals(object);
#     }
# }