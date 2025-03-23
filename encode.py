k = [1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298]


# Initial hash value
h0 = '01101010000010011110011001100111'
h1 = '10111011011001111010111010000101'
h2 = '00111100011011101111001101110010'
h3 = '10100101010011111111010100111010'
h4 = '01010001000011100101001001111111'
h5 = '10011011000001010110100010001100'
h6 = '00011111100000111101100110101011'
h7 = '01011011111000001100110100011001'

# função para fazer o rotate para direita
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

# função para somar dos binarios em w
def soma(w0, sigma0, w9, sigma1, i):
    novo_bin = bin(w0 + sigma0 + w9 + sigma1)

    novo_bin = novo_bin[2:]

    if(len(novo_bin) > 32):
        novo_bin = novo_bin[-32:]
    while(len(novo_bin) != 32):
        novo_bin = '0' + novo_bin 

    return novo_bin




def majority(bin_a, bin_b, bin_c):
    int_a = int(bin_a,2)
    int_b = int(bin_b,2)
    int_c = int(bin_c,2)


    majority = (int_a & int_b) ^ (int_a & int_c) ^ (int_b & int_c)
    return majority

def choice(bin_e, bin_f, bin_g):
    int_e = int(bin_e,2)
    int_f = int(bin_f,2)
    int_g = int(bin_g,2)

    choice = (int_e & int_f) ^ (~(int_e) & int_g)
    return choice

def xorE(bin_e):
    return (int(rightRotate(bin_e,6),2) ^ int(rightRotate(bin_e,11),2)) ^ (int(rightRotate(bin_e,25),2))

def xorA(bin_a):
    return (int(rightRotate(bin_a,2),2) ^ int(rightRotate(bin_a,13),2)) ^ (int(rightRotate(bin_a,22),2))

def temp1(bin_h, xorE, choice, k0, bin_w):
    int_h = int(bin_h,2)
    int_w = int(bin_w,2)
    soma = int_h + xorE + choice + k0 + int_w
    soma = bin(soma)
    soma = soma[2:]
    if(len(soma) > 32):
        soma = soma[-32:]
    while(len(soma) < 32):
        soma = '0' + soma 
    soma = int(soma,2)
    return soma

def temp2(majority, xorA):
    soma = majority + xorA
    soma = bin(soma)
    soma = soma[2:]
    if(len(soma) > 32):
        soma = soma[-32:]
    while(len(soma) < 32):
        soma = '0' + soma 
    soma = int(soma,2)
    return soma

def newA(temp1, temp2):
    soma = temp1 + temp2
    soma = bin(soma)
    soma = soma[2:]
    if(len(soma) > 32):
        soma = soma[-32:]
    while(len(soma) < 32):
        soma = '0' + soma 
    return soma

def newE(bin_d, temp1):
    int_d = int(bin_d,2)

    soma = int_d + temp1
    soma = bin(soma)
    soma = soma[2:]
    if(len(soma) > 32):
        soma = soma[-32:]
    while(len(soma) < 32):
        soma = '0' + soma 
    return soma




def operacaoSha256(w, original, a, b, c, d, e, f, g, h, h0, h1, h2, h3, h4, h5, h6, h7):
    for i in range(len(original)):
        if(i % 32 == 0):
            w.append(original[i:(i+32)])


    while(len(w) != 64):
        w.append('00000000000000000000000000000000')


    for i in range(16,len(w)):
        sigma0 = (int(rightRotate(w[i-15],7), 2) ^ int(rightRotate(w[i-15],18), 2)) ^ (int(w[i-15], 2) >> 3)
        

        sigma1 = (int(rightRotate(w[i-2],17), 2) ^ int(rightRotate(w[i-2],19), 2)) ^ ((int(w[i-2],2)) >> 10)
        
    
        w[i] = soma(int(w[i-16],2), sigma0, int(w[i-7],2), sigma1, i)

    for i in range(64):
        temporario1 = temp1(h, xorE(e), choice(e,f,g), k[i], w[i])
        temporario2 = temp2(majority(a,b,c), xorA(a))

        bin_d = d

        h = g
        g = f
        f = e
        e = newE(bin_d, temporario1)
        d = c
        c = b
        b = a
        a = newA(temporario1, temporario2)

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

    return (h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7)

original = 'recebaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' + chr(128)
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

for i in range(0,len(original),512):

    # Working Variables
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    f = h5
    g = h6
    h = h7

    messegeBlock = original[i:(i+512)]
    w = []
    sha256 = operacaoSha256(w, messegeBlock, a, b, c, d, e, f, g, h, h0, h1, h2, h3, h4, h5, h6, h7)
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
    
print(sha256)


