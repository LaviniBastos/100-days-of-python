def interseccao(lista1, lista2):
    return list(set(lista1) & set(lista2))

first_list = [1, 2, 3, 6, 8]
second_list = [6, 7, 8, 9, 10]


print(interseccao(first_list, second_list))