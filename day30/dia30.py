def anagrama(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())


palavra1 = input("Digite uma palavra e depois outra para verificarmos se elas são anagramas: ")
palavra2 = input("Digite a outra palavra: ")

resultado = anagrama(palavra1, palavra2)
if resultado == True:
    print("As palavras são um anagrama")
else:
    print("Infelizmnte elas não são um anagrama")