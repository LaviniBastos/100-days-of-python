import random

inicio = int(input("Digite  numero inicial: "))
fim = int(input("Digite o numero final: "))

aleatorio = random.randint(inicio, fim)
print(f"Numero aleario entre {inicio} e {fim} é: {aleatorio}")