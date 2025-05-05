
people = {
    "Ana": 40,
    "Bia": 43,
    "joão": 29
}

##Acessar os valores
print(people["Ana"])
print(people.get("joão"))
print(people.get("Alice", "Não encontrado"))

#Atualizar e adicionar itens

people["Ana"] = 30 #Atualizando a idade da Ana
people["Daniel"] = 50 #Adiciona um novo item no dicionário

#Removendo

people.pop("Daniel")  #removendo o item 
del people["Ana"] #outra forma de remover

#Para iterar sobre o dicionario

for nome, idade in people.items():
    print(f"{nome} tem {idade} anos")