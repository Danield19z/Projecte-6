#Programa fet per Daniel Torres
#Data: 13/01/2026
#Versio: 2.1
#Creacio d'una classe Punt amb mètodes per calcular la distància.
class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre):
        dx = self.x - altre.x
        dy = self.y - altre.y
        return (dx**2 + dy**2)**0.5

    def mostrar(self):
        return f"({self.x}, {self.y})"






