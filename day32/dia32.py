def  frase_invertida(palavras):
    palavra = palavras.split()
    frase_invertida = palavra[::-1]
    return ' '.join(frase_invertida)


frase = "estamos todos aqui agora!"
print(frase_invertida(frase))