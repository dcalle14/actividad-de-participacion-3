import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def calcular_perimetro(self):
        base = abs(self.esquina1.x - self.esquina2.x)
        altura = abs(self.esquina1.y - self.esquina2.y)
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina1.x - self.esquina2.x)
        altura = abs(self.esquina1.y - self.esquina2.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina1.x - self.esquina2.x)
        altura = abs(self.esquina1.y - self.esquina2.y)
        return base == altura

esquina1 = Punto(1, 1)
esquina2 = Punto(4, 5)
rectangulo1 = Rectangulo(esquina1, esquina2)

print("Perímetro del rectángulo:", rectangulo1.calcular_perimetro())
print("Área del rectángulo:", rectangulo1.calcular_area())

if rectangulo1.es_cuadrado():

    print("Área del rectángulo es un cuadrado")
else:
    print("Área del rectángulo no es un cuadrado")