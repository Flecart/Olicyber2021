#! /usr/bin/env python3
#region
def encryptData(param_1):
    param_1 = list(param_1)
    cicli = lvl1(param_1);
    print("/\\/\\/\\/\\/\\ LVL 1: Completato /\\/\\/\\/\\/\\");

    cicli = lvl2(cicli); # cicli contiene il testo cifrato a met`a
    print("/\\/\\/\\/\\/\\ LVL 2: Completato /\\/\\/\\/\\/\\");

    ans = lvl3(cicli);
    print("/\\/\\/\\/\\/\\ LVL 3: Completato. PEW PEW /\\/\\/\\/\\/\\");
    return ans

def lvl1(param_1):

    counter = 0;
    while (counter < len(param_1)):
        answer = ord(param_1[counter]);
        if (answer < ord('d')):
            answer = answer + -0x14
        else:
            answer = answer + ord('d');
        param_1[counter] = answer;
        counter = counter + 1;

    return param_1; 

def lvl2(param_1):

    strangeVariable = []

    offset = 0;
    counter = 0;
    while (counter < len(param_1)):
        
        buffer = param_1[counter]
        bufferLen = len(str(buffer))
        secondBuffer = bufferLen

        for x in str(secondBuffer):
            strangeVariable.append(x)

        for x in str(buffer):
            strangeVariable.append(x)
        counter = counter + 1;
    
    param_1 = "".join(strangeVariable)
    
    return param_1;

def lvl3(param_1):
    plaintext = []
    counter = 0;
    while (counter < len(param_1)):
        plaintext.append(param_1[(len(param_1) - counter) + -1])
        counter = counter + 1;
    return "".join(plaintext)
#endregion

# parte di decrypt
#region
def lvl2Decrypt(flag):
    
    ans = []
    counter = 0
    while counter < len(flag):
        lunghezza = int(flag[counter])
        numeri = flag[counter+1:counter+1+lunghezza]
        ans.append(int(numeri))
        counter += lunghezza + 1

    return ans

def lvl1Decrypt(flag):
    ans = []

    for x in flag:
        if x < ord('d'):
            ans.append(chr(x + 0x14))
        else:
            ans.append(chr(x - ord('d')))

    return ans


def decryptData(flag):
    ciclo1 = lvl3(flag) # inverte soltanto, ez
    ciclo2 = lvl2Decrypt(ciclo1)
    ciclo3 = lvl1Decrypt(ciclo2)
    return "".join(ciclo3)

#endregion
flag = 'flag{OwO-https://youtu.be/dQw4w9WgXcQ}'
ciphredFlag = '522322238023102381231023652522102341238229023572002300237725721123462522002313213201235725725729023752902340233223302377280232023'
# 522316297286230237627329123232912316200237221023872622712361237123112312237227228325123212361236123402352295291239523223302377280232023
# 522322238023102381231023652522102341238229023572002300237725721123462522002313213201235725725729023752902340233223302377280232023
print(encryptData(flag))
print(decryptData(ciphredFlag))

#reversato con successo!
# flag{hmMm___n33d-To_add_m0re-Levelz}