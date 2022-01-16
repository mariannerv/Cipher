def char2idx(c):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet.index(c)

def idx2char(i):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alfabeto[i]

def encodeCypher1(msg):
    
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    lista = [char for char in msg]
    
    for i in range(len(lista)):
            lista[i] = alfabeto[char2idx(lista[i]) - 5]

    return ''.join(lista)
    
def decodeCypher1(msg):
    
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    lista = [char for char in msg]
    
    for i in range(len(lista)):
        if char2idx(lista[i]) + 5 > 25:
            lista[i] = alfabeto[char2idx(lista[i]) + 5 -26]
            
        else:
            lista[i] = alfabeto[char2idx(lista[i]) + 5]

    return ''.join(lista)



def auxiliar(msg):
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    lista = [char for char in msg]
    
    for i in range(len(lista)):
        if char2idx(lista[i]) + 1 > 25:
            lista[i] = alfabeto[char2idx(lista[i]) + 1 -26]
            
        else:
            lista[i] = alfabeto[char2idx(lista[i]) + 1]

    return ''.join(lista)

def tabulaKey():
    res = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']

    for i in range(25):
        res.append(auxiliar(res[i]))

    return res


def encodeCypher2(msg):
    
    res = []
    
    for i in range(len(msg)):
        if i > 25:
            res.append(tabulaKey()[char2idx(msg[i])][i - 26])
        else:
            res.append(tabulaKey()[char2idx(msg[i])][i])
            
    return ''.join(res)




def criaChave(key, msg):

        chave = list(key)
        if len(msg) == len(chave):
            return chave
        else:
            for i in range(len(msg) - len(chave)):
                chave.append(chave[i % len(chave)])
        return  "" . join(chave)


def encodeCypher3(key, msg):

    res = []

    for i in range(len(msg)):
        res.append(tabulaKey()[char2idx(criaChave(key,msg)[i])][char2idx(msg[i])])
    return ''.join(res)
           

def decodeCypher3(key, msg):
    
    res = []

    for i in range(len(msg)):
        linha = tabulaKey()[char2idx(criaChave(key,msg)[i])]
        coluna = linha.find(msg[i])
        res.append(tabulaKey()[0][coluna])
    return ''.join(res)


def cifraMensagem(msg):
    semDuplicados =  "".join(dict.fromkeys(msg))
    substituiY = semDuplicados.replace("Y", "I")
    return substituiY

def criaMatrix(key):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXZ'
    matrix = [[0 for i in range (5)] for j in range(5)] # cria a matrix 5x5
    chaveFinal = cifraMensagem(key) #remove caracteres duplicados e substitui 'Y' por 'I'
    res = []


    #Aqui vamos juntar a chave criada mais o resto do alfabeto à lista vazia

    for c in chaveFinal:
        res.append(c)

    for a in alfabeto:
        if a not in chaveFinal:
            res.append(a)

    index = 0
    #Aqui criamos a matriz pela qual vamos iterar
    
    for i in range(0,5):
        for j in range(0,5):
            matrix[i][j] = res[index]
            index+=1

    return matrix



def encontraIndex(char, matriz):

    res = []

    for i, j in enumerate(matriz):
        for m, n in enumerate(j):       
            if char == n:
                res.append(i)
                res.append(m)
                return res
    

def encodeCypher4(key,msg):
    chaveFinal = cifraMensagem(key)
    matriz = criaMatrix(chaveFinal)
    msgFinal = msg.replace("Y", "I")
    res = []

    for letra in list(msgFinal):
        res.append(encontraIndex(letra,matriz))

    juntaListas = [j for i in res for j in i]
    listaToString = [str(k) for k in juntaListas]
    return ''.join(listaToString)

#print(encodeCypher4('LTI', 'PYTHON'))
    
def decodeCypher4(key,msg):
    chaveFinal = cifraMensagem(key)
    matriz = criaMatrix(chaveFinal)
    res = []

    caracteres = [int(char) for char in msg]
    linhas, colunas = caracteres[::2], caracteres[1::2]
    
    for i,j in zip(linhas,colunas):
        res.append(matriz[i][j])

    return ''.join(res)

#print(decodeCypher4('LTI', '310201203024')

def encodeCypher5(msg):
    

    return ''