def palavraUpper(palavra):
    palavraUpp=palavra.upper()
    return palavraUpp

def removeEspace(palavra):
    palavraJunta = ""
    for letra in palavra:
        if (letra != " "):
            palavraJunta += letra
    return palavraJunta

def getSpace(palavra):
    spaces = []
    for i, letra in enumerate(palavra):
        if letra == " ":
            spaces.append(i)
    return spaces
        

def setSpaces(stringJuntas, spaces):
    palavraSeparada = ""
    c = 0  
    j = 0  
    
    for i in range(len(stringJuntas) + len(spaces)):
        if c < len(spaces) and i == spaces[c]:
            palavraSeparada += " "
            c += 1
        elif j < len(stringJuntas):
            palavraSeparada += stringJuntas[j]
            j += 1
    
    return palavraSeparada


def divideString(palavraJunta):
    str1 = ""
    str2 = ""
    tamanho = len(palavraJunta)
    if((tamanho/2) % 2 != 0):
        palavraJunta +=" "
        
    for i, letra in enumerate(palavraJunta):
        if(i < (tamanho/2)):
            str1 += letra
        else:
            str2 += letra
            
    return str1,str2


def criptografar(p):
    palavra = palavraUpper(p)
    str1 =""
    str2 = ""
    palavraJunta = removeEspace(palavra)
    
    for i, letra in enumerate(palavraJunta):
        if i % 2 == 0:
            str1 += letra
        else:
            str2 += letra
    
    space = getSpace(p)
    stringJuntas = str1 + str2
    palavraCripto = setSpaces(stringJuntas,space)

    print("string 1: ",str1)
    print("string 2: ",str2)
    return palavraCripto



def decriptografar(criptografia):
    novaPalavra = ""
    spaces = getSpace(criptografia)
    palavraJunta = removeEspace(criptografia)
    stringDividida = divideString(palavraJunta)
    str1 = stringDividida[0]
    str2 = stringDividida[1]
    
    i = 0
    c = 0
    j = 0
    while (i <= len(palavraJunta)):
        if (c < len(str1)):
            novaPalavra += str1[c]
            c += 1
        if (j < len(str2)):
            novaPalavra += str2[j]
            j += 1
        i += 1
    
    novaPalavra =  setSpaces(novaPalavra,spaces)
    return novaPalavra



palavra = input("Digite uma palavra: ")

criptografia = (criptografar(palavra))
print("Palavra criptografada: ",criptografia)

PalavraConvertida = decriptografar(criptografia)
print("Palavra decriptografada: ",PalavraConvertida)