k = [1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298]

# Função para fazer o rotate para direita
def rightRotate(n_bin, rot):
    # Recebo um número em formato binário e tranformo em decimal
    n = int(n_bin, 2)
    # Guardo o final do número binário baseado no número de rotações
    final_bin = n_bin[-(rot):]
    # Realizo o shift para a direita
    numRot = n >> rot

    # Pego o resultado do número depois do shift e tranformo ele em binario
    numRot_bin = bin(numRot)
    numRot_bin = numRot_bin[2:]
    # Caso ele tenha menos de 32 caracteres e vou adicionando zeros
    while(len(numRot_bin) < 32):
        numRot_bin = '0' + numRot_bin
    # Pego o número que eu tinha salvo ali em cima e coloco ele na frente do binário shiftado
    numRot_bin = final_bin + numRot_bin[rot:]
    return numRot_bin

# Função para calcular o valor do novo w
def soma(w, sigma0, w9, sigma1):
    novo_bin = bin(w + sigma0 + w9 + sigma1)
    novo_bin = novo_bin[2:]
    # Caso o binário tenha mais de 32 caracteres eu ignoro os que estão a mais
    if(len(novo_bin) > 32):
        novo_bin = novo_bin[-32:]
    # Caso o binário tenha menos de 32 caracteres eu adiciono zeros no começo
    while(len(novo_bin) < 32):
        novo_bin = '0' + novo_bin 
    return novo_bin

# Função para calcular o número majority
def majority(bin_a, bin_b, bin_c):
    # Transformo os binários para descimal
    int_a = int(bin_a,2)
    int_b = int(bin_b,2)
    int_c = int(bin_c,2)

    # Faço um (A and B) XOR (A and C) XOR (B and C)
    majority = (int_a & int_b) ^ (int_a & int_c) ^ (int_b & int_c)
    return majority

# Função para calcular o número choice
def choice(bin_e, bin_f, bin_g):
    # Transformo os binários para descimal
    int_e = int(bin_e,2)
    int_f = int(bin_f,2)
    int_g = int(bin_g,2)

    # Faço um (E and F) XOR ((not E) and G)
    choice = (int_e & int_f) ^ (~(int_e) & int_g)
    return choice

# Função para calcular os xors de E
def xorE(bin_e):
    # Faço um (E rigthRotate(6)) XOR (E rigthRotate(11)) XOR (E rigthRotate(25))
    return (int(rightRotate(bin_e,6),2) ^ int(rightRotate(bin_e,11),2)) ^ (int(rightRotate(bin_e,25),2))

# Função para calcular os xors de A
def xorA(bin_a):
    # Faço um (E rigthRotate(2)) XOR (E rigthRotate(13)) XOR (E rigthRotate(22))
    return (int(rightRotate(bin_a,2),2) ^ int(rightRotate(bin_a,13),2)) ^ (int(rightRotate(bin_a,22),2))

# Função para calcular o número temporário 1
def temp1(bin_h, xorE, choice, k0, bin_w):
    # Transformo os binários para descimal
    int_h = int(bin_h,2)
    int_w = int(bin_w,2)
    
    soma = int_h + xorE + choice + k0 + int_w
    soma = bin(soma)
    soma = soma[2:]
    # Caso o binário tenha mais de 32 caracteres eu ignoro os que estão a mais
    if(len(soma) > 32):
        soma = soma[-32:]
    # Caso o binário tenha menos de 32 caracteres eu adiciono zeros no começo
    while(len(soma) < 32):
        soma = '0' + soma 
    # transformo o número binário para decimal
    soma = int(soma,2)
    return soma

# Função para calcular o número temporário 2
def temp2(majority, xorA):
    soma = majority + xorA
    soma = bin(soma)
    soma = soma[2:]
    # Caso o binário tenha mais de 32 caracteres eu ignoro os que estão a mais
    if(len(soma) > 32):
        soma = soma[-32:]
    # Caso o binário tenha menos de 32 caracteres eu adiciono zeros no começo
    while(len(soma) < 32):
        soma = '0' + soma 
    # transformo o número binário para decimal
    soma = int(soma,2)
    return soma

# Função para calcular o novo valor de A
def newA(temp1, temp2):
    soma = temp1 + temp2
    soma = bin(soma)
    soma = soma[2:]
    # Caso o binário tenha mais de 32 caracteres eu ignoro os que estão a mais
    if(len(soma) > 32):
        soma = soma[-32:]
    # Caso o binário tenha menos de 32 caracteres eu adiciono zeros no começo
    while(len(soma) < 32):
        soma = '0' + soma 
    return soma

# Função para calcular o novo valor de E
def newE(bin_d, temp1):
    int_d = int(bin_d,2)

    soma = int_d + temp1
    soma = bin(soma)
    soma = soma[2:]
    # Caso o binário tenha mais de 32 caracteres eu ignoro os que estão a mais
    if(len(soma) > 32):
        soma = soma[-32:]
    # Caso o binário tenha menos de 32 caracteres eu adiciono zeros no começo
    while(len(soma) < 32):
        soma = '0' + soma 
    return soma

# Função com as operações que são realizadas em cada bloco
def operacaoSha256(w, original, a, b, c, d, e, f, g, h, h0, h1, h2, h3, h4, h5, h6, h7):
    # A variável original é uma string com os binarios da palavra
    # aqui eu transformo essa string em uma lista w,  com os binários seperados a cada 32 caracteres
    for i in range(len(original)):
        if(i % 32 == 0):
            w.append(original[i:(i+32)])

    # Caso a lista não tenha 64 itens
    # Adiciono novos itens com valores zerados
    while(len(w) != 64):
        w.append('00000000000000000000000000000000')

    # Aqui serão feitas as contas para determinar os novos valores das Working Variables
    # Como os valores da lista estão certos de w[0] até w[15]
    # Eu começo o i em 16 e vou até o tamanho de w (que é 64)
    for i in range(16,len(w)):
        # Faço um (w[i-15] rightRotate(7)) XOR (w[i-15] rightRotate(18)) XOR (w[i-15] >> 3))
        sigma0 = (int(rightRotate(w[i-15],7), 2) ^ int(rightRotate(w[i-15],18), 2)) ^ (int(w[i-15], 2) >> 3)
        # Faço um (w[i-2] rightRotate(17)) XOR (w[i-2] rightRotate(19)) XOR (w[i-2] >> 10))
        sigma1 = (int(rightRotate(w[i-2],17), 2) ^ int(rightRotate(w[i-2],19), 2)) ^ ((int(w[i-2],2)) >> 10)
        
        # O novo valor que vai par lista é a soma se w[i-16] mais o sigma0 mais w[i-7] mais sigma1
        w[i] = soma(int(w[i-16],2), sigma0, int(w[i-7],2), sigma1)

    # Aqui eu vou calcular as variáveis temporarias e colocar os novos valores nas variáveis
    for i in range(64):
        # chamo a função temp1 para fazer a soma
        temporario1 = temp1(h, xorE(e), choice(e,f,g), k[i], w[i])
        # chamo a função temp2 para fazer a soma
        temporario2 = temp2(majority(a,b,c), xorA(a))

        # Novos valores para as Working Variables
        h = g
        g = f
        f = e
        e = newE(d, temporario1) # Chamo a função para descobrir o novo valor de E
        d = c
        c = b
        b = a
        a = newA(temporario1, temporario2) # Chamo a função para descobrir o novo valor de A

    # Faz a soma das variaveis modificadas com as variveis iniciais
    # Transformo elas em hexadecimal
    h0 = int(h0,2) + int(a,2)
    h0 = bin(h0)
    h0 = h0[2:]
    if(len(h0) > 32):
        h0 = h0[-32:]
    while(len(h0) < 32):
        h0 = '0' + h0 
    h0 = hex(int(h0,2))
    h0 = h0[2:]
    while(len(h0) < 8):
        h0 = '0' + h0

    h1 = int(h1,2) + int(b,2)
    h1 = bin(h1)
    h1 = h1[2:]
    if(len(h1) > 32):
        h1 = h1[-32:]
    while(len(h1) < 32):
        h1 = '0' + h1 
    h1 = hex(int(h1,2))
    h1 = h1[2:]
    while(len(h1) < 8):
        h1 = '0' + h1

    h2 = int(h2,2) + int(c,2)
    h2 = bin(h2)
    h2 = h2[2:]
    if(len(h2) > 32):
        h2 = h2[-32:]
    while(len(h2) < 32):
        h2 = '0' + h2 
    h2 = hex(int(h2,2))
    h2 = h2[2:]
    while(len(h2) < 8):
        h2 = '0' + h2

    h3 = int(h3,2) + int(d,2)
    h3 = bin(h3)
    h3 = h3[2:]
    if(len(h3) > 32):
        h3 = h3[-32:]
    while(len(h3) < 32):
        h3 = '0' + h3 
    h3 = hex(int(h3,2))
    h3 = h3[2:]
    while(len(h3) < 8):
        h3 = '0' + h3

    h4 = int(h4,2) + int(e,2)
    h4 = bin(h4)
    h4 = h4[2:]
    if(len(h4) > 32):
        h4 = h4[-32:]
    while(len(h4) < 32):
        h4 = '0' + h4 
    h4 = hex(int(h4,2))
    h4 = h4[2:]
    while(len(h4) < 8):
        h4 = '0' + h4

    h5 = int(h5,2) + int(f,2)
    h5 = bin(h5)
    h5 = h5[2:]
    if(len(h5) > 32):
        h5 = h5[-32:]
    while(len(h5) < 32):
        h5 = '0' + h5 
    h5 = hex(int(h5,2))
    h5 = h5[2:]
    while(len(h5) < 8):
        h5 = '0' + h5

    h6 = int(h6,2) + int(g,2)
    h6 = bin(h6)
    h6 = h6[2:]
    if(len(h6) > 32):
        h6 = h6[-32:]
    while(len(h6) < 32):
        h6 = '0' + h6 
    h6 = hex(int(h6,2))
    h6 = h6[2:]
    while(len(h6) < 8):
        h6 = '0' + h6

    h7 = int(h7,2) + int(h,2) 
    h7 = bin(h7)
    h7 = h7[2:]
    if(len(h7) > 32):
        h7 = h7[-32:]
    while(len(h7) < 32):
        h7 = '0' + h7 
    h7 = hex(int(h7,2))
    h7 = h7[2:]
    while(len(h7) < 8):
        h7 = '0' + h7
    # Retorno uma string com todas juntas
    return (h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7)

# Recebe o caminho de um arquivo
def lerArquivo(path):
    arquivo_binario = ''
    # Lê o arquivo em binário
    f = open(path, 'rb')
    bina = f.read()
    palavra = [b for b in bina]
    f.close()

    # Aqui eu tiro o 0b que tem na frente do formato binário
    # Caso elas não tenham 8 caracteres eu adiciono zeros na frente
    # E por fim passo tudo para uma váriavel, para não precisar alterar o meu código
    for i in range(len(palavra)):
        palavra_completa = bin(palavra[i])
        palavra_completa = palavra_completa[2:]

        while(len(palavra_completa) < 8):
            palavra_completa = '0' + palavra_completa

        arquivo_binario = arquivo_binario + palavra_completa
    # Retorno uma string com todos os binários
    return arquivo_binario


# Função principal sha-256
def sha256(palavra, op):
    # Inicializo as variáveis
    size = ''
    letras_bin = ''
    letras = ''

    # Initial hash value
    h0 = '01101010000010011110011001100111'
    h1 = '10111011011001111010111010000101'
    h2 = '00111100011011101111001101110010'
    h3 = '10100101010011111111010100111010'
    h4 = '01010001000011100101001001111111'
    h5 = '10011011000001010110100010001100'
    h6 = '00011111100000111101100110101011'
    h7 = '01011011111000001100110100011001'

    if (op == 'f'):
        letras_bin = lerArquivo(palavra)

    if (op == 's'):
        # Nesse for eu tranformo cada letras da string para o formato binário
        for i in range(len(palavra)):
            for byte in palavra[i].encode('utf-8'):    
                letras = format(byte, 'b')
                # Caso o formato binário da letra tenha menos que 8 caracteres, e adiciono zeros até fechar 8
                while(len(letras) < 8):
                    letras = '0' + letras
                # Junto todos os binários das letras em uma string
                letras_bin = letras_bin + letras
        
    # Passo essa sting para a variável da palavra original
    # Porque eu ja tinha feito toda a lógica usando a palavra original   
    # Daí fiquei com preguiça de substituír para letras_bin em tudo 
    letras_bin = letras_bin + '10000000'
    original = letras_bin

    # Aqui eu vou ver quantos caracteres na palavra original, retiro os ultimos 8 caracteres q é do '10000000'
    # divido pro 8, pra saber esse tamanho em decimal, e tranformo esse decimal em binário
    size = bin(int(len(original[:-8])/8))
    # Adiciono '000' depois do tamanho da palavra em binário, porque sim
    size = size[2:] + '000'

    # Como o tamanho estava o binário do tamanho mais o '000'
    # Eu vou adicionando zeros até fechar os 64 bits necessários 
    while(len(size) != 64):
        size = '0' + size

    # Como essa criptografia funciona com blocos de 512 bits
    # Aqui eu pego o tamanho da palavra original mais 64 (esse 64 é o valor reservado para o tamanho, que são 64 bits)
    # E adiciono zeros até fechar o próximo múltiplo de 512
    while((len(original) + 64) % 512 != 0):
        original += '0'

    # Como eu basicamente deixei a variável original com o tamanho de (múltiplo de 512) - 64
    # Aqui eu adiciono os 64 bits do tamanho na variável original, agora o tamanho da original fica múltiplo de 512
    original = original + size

    # Conforme eu já escrevi ali em cima, essa criptográfia trabalha com blocos de 512 bits cada
    # Nesse for eu começo com o i = 0, ele vai até o tamanho da variável original(algum multiplo de 512)
    # E cada repetição desse for o i é incrementado 512
    for i in range(0,len(original),512):

        w = []

        # Working Variables
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7

        # Aqui eu separado os blocos de 512 bits para poderem ser feitas as operações
        messegeBlock = original[i:(i+512)]

        # Realizadas as operações, a função operaçãoSha256 vai retornar uma string dos hexadecimais dos valores dos Hs 
        sha256 = operacaoSha256(w, messegeBlock, a, b, c, d, e, f, g, h, h0, h1, h2, h3, h4, h5, h6, h7)
        # Como eu estou usando os Hs em formato binário
        # Como cada H retornou um valor hexadecimal de 8 caracteres, aqui eu pego a string e separo ela de 8 em 8
        # E adiciono esses valores hexadecimais nos respectivos Hs
        # Por fim transformo esses valores em binários de 32 caracteres para serem usados novamente se preciso
        h0 = sha256[:8]
        h0 = bin(int(h0, 16))
        h0 = h0[2:]
        while(len(h0) < 32):
            h0 = '0' + h0 

        h1 = sha256[8:16]
        h1 = bin(int(h1, 16))
        h1 = h1[2:]
        while(len(h1) < 32):
            h1 = '0' + h1 
        
        h2 = sha256[16:24]
        h2 = bin(int(h2, 16))
        h2 = h2[2:]
        while(len(h2) < 32):
            h2 = '0' + h2 
        
        h3 = sha256[24:32]
        h3 = bin(int(h3, 16))
        h3 = h3[2:]
        while(len(h3) < 32):
            h3 = '0' + h3 
        
        h4 = sha256[32:40]
        h4 = bin(int(h4, 16))
        h4 = h4[2:]
        while(len(h4) < 32):
            h4 = '0' + h4 
        
        h5 = sha256[40:48]
        h5 = bin(int(h5, 16))
        h5 = h5[2:]
        while(len(h5) < 32):
            h5 = '0' + h5 
        
        h6 = sha256[48:56]
        h6 = bin(int(h6, 16))
        h6 = h6[2:]
        while(len(h6) < 32):
            h6 = '0' + h6 
        
        h7 = sha256[56:64]
        h7 = bin(int(h7, 16))
        h7 = h7[2:]
        while(len(h7) < 32):
            h7 = '0' + h7
    # Quando o for terminar, será retornado a palavra criptografada certinho 100% sem erros correta atualizado 2025
    return sha256
