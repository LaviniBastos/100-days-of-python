############# Condicionais if e else simples, escrever um código ue verifica a maioridade de um usuário ################

idade = int(input("qual é a sua idade? "))

if idade >= 18:
    print("Você já é de maior! ")
else:
    print("Você ainda é de menor!")
    
################# If - Else aninhados: Escrever um programa para identificar qual numero de 3 é o maior####################

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 >= num2:
    if num1 >= num3:
        print(f"O numero maior é {num1}")
    else:
        print(f"o numero maior é {num3}")
else:
    if num2 >= num3:
        print(f"O numero maior é {num2}")
    else:
        print(f"o numero maior é {num3}")
        
#################Loop for: Escrever um programa que calcula a soma do numero inteiro inserido no input###############

num = int(input(" Digite um numero inteiro: "))
soma = 0

for n in range(1, num + 1 ):
    soma += n

print(f"A soma de todos os numeros de 1 a {num} é: {soma}")

################ While: Escrever um código que calcula o fatorial de um numero ###############

numero = int(input(" Digite um numero para calcular o seu fatorial: "))
fac = 1
while numero > 1:
    fac *= numero
    numero -= 1
    
print(f"O fatorial do numero inserido é : {fac}")