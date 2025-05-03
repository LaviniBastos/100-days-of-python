sets = {1, 2, 2, 3, 4, 4, 5, 5}
print("Set sem duplicidade: ", sets)

#Para adicionar ou remover um elemento do set

sets.add(6)
sets.discard(3)
sets.remove(2)

print("Set atualizado: ", sets)

#operações

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("União: ", a.union(b))
print("Intersecção: ", a.intersection(b))
print("Diferença: ", a.difference(b))

#para iterar sobre o set

for itens in sets:
    print("Item:", itens)