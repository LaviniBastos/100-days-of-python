def unindo_dicionarios(dic1, dic2):
    unindo = dic1.copy()
    unindo.update(dic2)
    return unindo


d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}


print(unindo_dicionarios(d1, d2))