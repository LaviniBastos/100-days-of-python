lista = ["morango", "pera", "maça", "abacaxi", "banana"]

#Iterando sobre a lista
for frutas in lista:
    print(frutas)
    
##################################
    
print("primeiro item da lista", lista[0]) # Acessando o item da posição 0 da lista
print("Terceiro item da lista", lista[3]) # Acessando o item da posição 3 da lista
print("Quarto item da lista", lista[4]) # Acessando o item da posição 4 da lista

###################################

#Adicionando um novo item na lista
lista.append("cereja")
print(lista)

#emoendo um item da lista
lista.remove("cereja")
print(lista)

##inserindo um novo em uma posição existente

lista.insert(2, "mamão")
print("o item: ", lista[2], "entrou na lista")
print("Lista atualizada: ", lista)
