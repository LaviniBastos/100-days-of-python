tabu = int(input("Qual numero você deseja saber a tabuada?"))
contagem = 0
for numeros in range(1, 11):
    numeros *= tabu
    if contagem <= 10:
        contagem += 1
    print(f"{tabu} x", contagem, "=", numeros)