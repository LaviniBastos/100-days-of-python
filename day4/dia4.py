# operações básicas

numero1 = 20
numero2 = 3

soma = numero1 + numero2
subtração = numero1 - numero2
multiplicação = numero1 * numero2
divisão = numero1 / numero2
floor = numero1 // numero2
modulos = numero1 % numero2
potencia = numero1 ** numero2

#Operadores relacionais

igual = numero1 == numero2
diferente = numero1 != numero2
maior_que = numero1 > numero2
menor_que = numero1 < numero2
maior_ou_igual = numero1 >= numero2
menor_ou_igual = numero1 <= numero2

# Operadores Lógicos

verdadeiro = True
falso = False

print("______Operadores aritméticos_____")
print(f"A soma entre {numero1} e {numero2} é: {soma}")
print(f"A diferença entre {numero1} e {numero2} é: {subtração}")
print(f"A multiplicação entre {numero1} e {numero2} é: {multiplicação}")
print(f"A divisão entre {numero1} e {numero2} é: {divisão}")
print(f"O numero mais baixo da divisão entre {numero1} e {numero2} é: {floor}")
print(f"O resto da divisão entre {numero1} e {numero2} é: {modulos}")
print(f"A potenciação entre {numero1} e {numero2} é: {potencia}")


print("_______Operadores Relacionais_________")
print(f"o numero {numero1} e {numero2} são iguais? {igual}")
print(f"o numero {numero1} e {numero2} são diferentes? {diferente}")
print(f"o numero {numero1} é maior que o numero: {numero2}? {maior_que}")
print(f"o numero {numero1} é menor que o numero: {numero2}? {menor_que}")
print(f"o numero {numero1} é maior ou igual ao numero: {numero2}? {maior_ou_igual}")
print(f"o numero {numero1} é menor ou igual ao numero: {numero2}? {menor_ou_igual}")

print("________Operadores Lógicos_________")
print("Verdadeiro E Falso: ", verdadeiro and falso)
print("Verdadeiro E verdadeiro: ", verdadeiro and verdadeiro)
print("Falso E Falso: ", falso and falso)
print("Verdadeiro OU Falso: ", verdadeiro or falso)
print("Verdadeiro OU verdadeiro: ", verdadeiro or verdadeiro)
print("Falso OU Falso: ", falso or falso)
print("Não Verdadeiro: ", not verdadeiro)
print("Não Falso: ", not falso)