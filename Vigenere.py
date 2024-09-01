alfabeto_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chave = "a"

def criptografar(palavra, chave):
    novaPalavra = ""
    palavra = palavra.upper()
    chave = chave.upper()
    
    chaveIndex = 0
    
    for letra in palavra:
        if letra == " ":
            novaPalavra += " "
            continue
        
        alfabetoIndex = alfabeto_maiusculas.index(letra)
        indice_ciclico = chaveIndex % len(chave)
        caractere_chave = chave[indice_ciclico]
        chaveIndexAlfabeto = alfabeto_maiusculas.index(caractere_chave)
        
        criptIndex = (alfabetoIndex + chaveIndexAlfabeto) % 26
        
        novaPalavra += alfabeto_maiusculas[criptIndex]
        
        chaveIndex += 1
    
    return novaPalavra

def decriptografar(palavra, chave):
    novaPalavra = ""
    palavra = palavra.upper()
    chave = chave.upper()
    
    chaveIndex = 0
    
    for letra in palavra:
        if letra == " ":
            novaPalavra += " "
            continue
        
        alfabetoIndex = alfabeto_maiusculas.index(letra)
        indice_ciclico = chaveIndex % len(chave)
        caractere_chave = chave[indice_ciclico]
        chaveIndexAlfabeto = alfabeto_maiusculas.index(caractere_chave)
        
        decriptIndex = (alfabetoIndex - chaveIndexAlfabeto + 26) % 26
        
        novaPalavra += alfabeto_maiusculas[decriptIndex]
        
        chaveIndex += 1
    
    return novaPalavra

palavra = input("Digite uma palavra: ")
palavraCripto = criptografar(palavra, chave)
print("Mensagem criptografada: ", palavraCripto)
print("Mensagem decriptografada:", decriptografar(palavraCripto, chave))
