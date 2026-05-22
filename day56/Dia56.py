#Sets em python

#Criação dos conjuntos. (Ele não permite números duplicados)

conjuntoA = {1,2,3,67,9,8}
conjuntoB = {2,3,1,4,2,5,3,4}
print("Resultado dos conjuntos")
print(f"Conjunto A: {conjuntoA}")
print(f"Conjunto B: {conjuntoB}")

# Unindo os conjuntos ( valores iguais não repetem )
unindo = conjuntoA.union(conjuntoB)
print(f"União: {unindo}")

# Intersecção (irá imprimir somente os valores que existem nos dois conjuntos)
inter = conjuntoA.intersection(conjuntoB)
print(f"Intersecção {inter}")

# Diferença (Pega os elementos únicos dos conjuntos)
difff = conjuntoA.difference(conjuntoB)
print(f"Diferença: {difff}")

# A diferença simétrica vai pegar os valores que não estão em ambos
symmetric_difff = conjuntoA.symmetric_difference(conjuntoB)
print(f"Diferença simétrica: {symmetric_difff}")