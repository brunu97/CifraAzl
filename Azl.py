#           #
# Cifra Azl #
#           #
# Cifra criada por - Bruno Silva 2021

def Cifra(msg, senha):
    chaveSomada = 0
    lista = []
    for s in senha: # Gera Chave
        chaveSomada = chaveSomada + ord(s)

    for x, i in enumerate(msg): # Cifra mensagem
        if x % 2 == 0:
            v = ord(i) * (chaveSomada + x)
        else:
            v = ord(i) * (chaveSomada - x)
        lista.append(str(v))
    
    m = max(map(len, lista)) # Adiciona 0s para garantir de cada elemento seja do mesmo tamanho
    for x, i in enumerate(lista):
        lista[x] =  "0"*(m - len(i)) + i
        

    return '/'.join(lista)


def Decifra(cifra, senha):
    m = len(cifra.split("/")[0])
    cifra = cifra.replace("/", "")
    
    cd = [cifra[i:i+m] for i in range(0, len(cifra), m)]
    lista = []
    chaveSomada = 0

    for s in senha: # Gera Chave
        chaveSomada = chaveSomada + ord(s)

    for x, i in enumerate(cd): # Decifra
        if x % 2 == 0:
            v = chr(int(int(i) / (chaveSomada + x)))
        else:
            v = chr(int(int(i) / (chaveSomada - x)))
        lista.append(str(v))

    return ''.join(lista)
