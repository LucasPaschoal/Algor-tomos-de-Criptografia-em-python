#variáveis globais
dicio = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","X","Y","Z"
chave = 3

def palavraUpper(p):
    palavraUpp=palavra.upper()
    return palavraUpp

def criptografar(p,chave,dicio):
    palavra = palavraUpper(p)
    nova_palavra = ""

    for letra in palavra:
        if letra in dicio:
            indice = dicio.index(letra)
            indice += chave;
            while (indice > len(dicio)):
                indice -= len(dicio)
            nova_palavra += dicio[indice]
        else:
            nova_palavra += letra
            
    return nova_palavra

def descriptografar(palavra,chave,dicio):
    nova_palavra = ""

    for letra in palavra:
        if letra in dicio:
            indice = dicio.index(letra)
            indice -= chave
            while(indice < 0):
                indice += len(dicio) 
            nova_palavra += dicio[indice]
        else:
            nova_palavra += letra
            
    return nova_palavra


palavra = input("Digite uma palavra: ")
palavra_formada = criptografar(palavra,chave,dicio)
print(palavra_formada)
print(descriptografar(palavra_formada,chave,dicio))