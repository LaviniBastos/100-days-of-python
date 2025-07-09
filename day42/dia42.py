import math

#Classe principal
class Forma:
    def area(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

# Subclasses
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


formas = [
    Circulo(3),
    Quadrado(4),
    Triangulo(6, 2)
]

for forma in formas:
    print(f"Área: {forma.area():.2f}")