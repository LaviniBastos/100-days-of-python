
print("Vamos descobrir para você o maior numero de 3:")
num1 = int(input("Digite o primeiro numero"))
num2 = int(input("Digite o segundo numero"))
num3 = int(input("Digite o terceiro numero"))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3
    
print(f" O maior numero é: {maior}")