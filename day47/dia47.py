class Animal:
    def emitindo_som(self):
        print("Cada animal faz um som")
        
class Cao(Animal):
    def emitindo_som(self):
        print("O cachorro irá latir")
        
class Gato(Animal):
    def emitindo_som(self):
        print("O gato irá miar")
        
class Galo(Animal):
    def emitindo_som(self):
        print("O Galo vai cantar")
        

def som_do_animal(animal):
    animal.emitindo_som()
        
animais = [Cao(), Gato(), Galo()]
for animal in animais:
    som_do_animal(animal)