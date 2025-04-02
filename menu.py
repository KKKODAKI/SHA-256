import encode
import os

escolha = 1

while(escolha):
    os.system('cls')

    print('===========================')
    print('1 - Criptografar palavra')
    print('2 - Criptografar documento')
    print('3 - Validar documento')
    print('0 - Sair')
    print('===========================')

    escolha = int(input('Digite: '))

    if(escolha == 1):
        os.system('cls')
        palavra = input('Digite uma palavra: ')
        os.system('cls')

        encoded = encode.sha256(palavra, 's')

        print('original: ' + palavra)
        print('\ncriptografada: ' + encoded)

        print('\n1 - Continuar')
        print('0 - Sair')
        escolha = int(input('Digite: '))

    if(escolha == 2):
        os.system('cls')
        path = input('Digite o nome do arquivo: ')
        encoded = encode.sha256(path, 'f')

        print('\nassinatura: ' + encoded)

        pathKey = path + '-Key.txt'
        f = open(pathKey, 'w', encoding='utf-8')
        f.write(encoded)
        f.close()

        print('\n1 - Continuar')
        print('0 - Sair')
        escolha = int(input('Digite: '))

    if escolha == 3:
        os.system('cls')
        path = input("Digite o nome do arquivo: ")
        encoded = encode.sha256(path, 'f')

        pathKey = path + '-Key.txt'
        f = open(pathKey, 'r', encoding='utf-8')
        key = f.read()
        f.close()

        if(encoded == key):
            print('Arquivo original')
        else:
            print('Arquivo alterado!!!')

        print('\n1 - Continuar')
        print('0 - Sair')
        escolha = int(input('Digite: '))
