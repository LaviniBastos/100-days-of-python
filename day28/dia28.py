def frequencia_palavra(frase):
    palavras = frase.lower().split()
    frequencia = {}
    for palavra in palavras:
        palavra = palavra.strip('.,!?') 
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    return frequencia

texto = "Python é muito muito muito divertido, e temos muitas muitas oportunidades de criar criar e criar"
print(frequencia_palavra(texto))
