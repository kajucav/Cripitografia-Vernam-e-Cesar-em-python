def criptografiaCesar(mensagem, key):
    letras = "abcdefghijklmnopqrstuvwxyz"
    encadear = ""

    for i in mensagem:
        if i in letras:
            encadearLetras = (ord(i) - ord('a') + key) % 26
            encadear += letras[encadearLetras]
        else:
            encadear += i  
            
    return encadear
    

def descriptaCesar(crypt, key):
    letras = "abcdefghijklmnopqrstuvwxyz"
    decriptaMensagem = ""

    for i in crypt:
        if i in letras:
            desencadearLetras = (ord(i) - ord('a') - key) % 26
            decriptaMensagem += letras[desencadearLetras]
        else:
            decriptaMensagem += i 
    
    return decriptaMensagem

mensagem = "vocevaiseratacado"
cryptoMensagem = criptografiaCesar(mensagem, 10)
decriptaMensagem = descriptaCesar(cryptoMensagem, 10)
print(cryptoMensagem)
print(decriptaMensagem)
