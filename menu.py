import encode
import os


os.system('cls')
palavra = input("Digite uma palavra: ")
os.system('cls')

encoded = encode.sha256(palavra)

print('original: ' + palavra)
print('\ncriptografada: ' + encoded)
