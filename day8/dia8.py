tuplas = ("Django", 2.0, False, 55)

#Para acessar os elementos
print("Primero item", tuplas[0])
print("Último item", tuplas[-1])

#operação com tuplas
another = ("nops",)
tupla_dupla = tuplas + another
print ("Tuplas concatenadas", tupla_dupla)

# Repetida

mult = tuplas * 2
print("Tupla multiplicada por 2: ", mult)

print ( "Existe 'Django' na tupla?", "Django" in tuplas)

# Converter tuplas em listas

lista = list(tuplas)
lista[1] = 4.0
tupla_modificada = tuple(lista)
print("A tupla foi modificada porque foi convertida em uma lista: ", tupla_modificada)