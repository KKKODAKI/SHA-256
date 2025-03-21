original = 'receba' + chr(128)
letras_bin = ''
size = ''
size = bin(len(original[:-1]))
size = size[2:] + '000'
w = []


def rightRotate(n_bin, rot):
    n = int(n_bin, 2)
    final_bin = n_bin[-(rot):]
    numRot = n >> rot

    numRot_bin = bin(numRot)
    numRot_bin = numRot_bin[2:]
    while(len(numRot_bin) != 32):
        numRot_bin = '0' + numRot_bin
    numRot_bin = final_bin + numRot_bin[rot:]

    return numRot_bin

def soma(w0, sigma0, w9, sigma1, i):
    novo_bin = bin(w0 + sigma0 + w9 + sigma1)

    novo_bin = novo_bin[2:]

    if(len(novo_bin) > 32):
        novo_bin = novo_bin[-32:]
    while(len(novo_bin) != 32):
        novo_bin = '0' + novo_bin 

    return novo_bin


for i in range(len(original)):
    letras = format(ord(original[i]), 'b')
   
    if (len(letras)==8):
        letras_bin = letras_bin+  letras

    elif(len(letras)==7):
        letras_bin = letras_bin + '0' + letras
 
    elif(len(letras)==6):
        letras_bin = letras_bin + '00' + letras


original = letras_bin


while(len(size) != 64):
    size = '0' + size


while((len(original) + 64) % 512 != 0):
    original += '0'


original = original + size


for i in range(len(original)):
    if(i % 32 == 0):
        w.append(original[i:(i+32)])


while(len(w) != 64):
    w.append('00000000000000000000000000000000')


for i in range(16,len(w)):
    sigma0 = (int(rightRotate(w[i-15],7), 2) ^ int(rightRotate(w[i-15],18), 2)) ^ (int(w[i-15], 2) >> 3)
    

    sigma1 = (int(rightRotate(w[i-2],17), 2) ^ int(rightRotate(w[i-2],19), 2)) ^ ((int(w[i-2],2)) >> 10)
    
 
    w[i] = soma(int(w[i-16],2), sigma0, int(w[i-7],2), sigma1, i)


print(w)


