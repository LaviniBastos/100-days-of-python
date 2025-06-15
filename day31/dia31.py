def palavra_longa(palavra):
    palavras = palavra.split()
    return max(palavras, key=len)

frase = input("Digite uma frase e vamos te dizer qual é a palavra mais longa dela: ")

print(palavra_longa(frase))
    