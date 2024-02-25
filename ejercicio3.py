import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas: ({self.x}, {self.y})")

    def mover(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia

punto1 = Punto(3, 4)
punto2 = Punto(6, 8)

punto1.mostrar()
punto2.mostrar()

distancia = punto1.calcular_distancia(punto2)
print("Distancia entre los puntos:", distancia)

punto1.mover(5, 5)
punto1.mostrar()