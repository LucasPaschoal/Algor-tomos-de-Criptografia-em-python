def palavraUpper(palavra):
    palavraUpp=palavra.upper()
    return palavraUpp


def criptografar(palavra):
    palavraUpp = palavraUpper(palavra)
    
    dicio = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","X","Y","Z"
    chave = "B","A","D","C","F","E","H","G","J","I","L","K","N","M","P","O","S","R","U","T","X","V","Z","Y"
    
    nova_palavra = ""
    for letra in palavraUpp:
        if letra in dicio:
            indice = dicio.index(letra)
            nova_palavra += chave[indice]
        else:
            nova_palavra += letra
            
    return nova_palavra

def descriptografar(palavra):
    return criptografar(palavra)


palavra = input("Digite uma palavra: ")
palavra_formada = criptografar(palavra)
print(palavra_formada)
print(descriptografar(palavra_formada))