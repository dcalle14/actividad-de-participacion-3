import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2)
        return distancia_centro_punto <= self.radio


centro = Punto(0, 0)
circulo1 = Circulo(centro, 5)

print("Área del círculo:", circulo1.calcular_area())
print("Perímetro del círculo:", circulo1.calcular_perimetro())

punto1 = Punto(3, 3)
if circulo1.punto_pertenece(punto1):
    print("El punto pertenece al círculo")
else:
    print("El punto no pertenece al círculo")


