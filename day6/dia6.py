
#### função simples ####
def great_user(name):
    return print(f"hello {name}")

great_user("Laviii")
print()

########### Função com um parametro padrão #########

def great_user(name='Guest'):
    return print(f"Helloo, {name}")

great_user()

########## Calcular um retangulo ###########

def retan(length, breadth):
    return length * breadth

print("A área do retangulo é: ", retan(6, 9))

###### modificando variavel global e local

f = 4
print(f"O valor da variável inicial é: {f}")

def modifica_local():
    f = 10
    print("valor de f dentro da função local: ", f)
    
def modifica_global():
    global f 
    f = 20
    
    print("Valor de f dentro da função global", f)

modifica_local()
modifica_global()
