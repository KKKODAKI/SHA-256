original = 'receba' + chr(128)
letras_bin = ''
size = ''
size = bin(len(original[:-1]))
size = size[2:] + '000'

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

'''
binario_arrumado = ''
for i in range(len(original)):
    if(i % 8 == 0):
        if(i % 32 == 0):
            binario_arrumado = binario_arrumado + '\n'
        binario_arrumado = binario_arrumado + ' ' + original[i:(i+8)]
print(binario_arrumado)
'''

print(original)
        

