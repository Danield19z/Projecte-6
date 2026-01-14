#Programa fet per Daniel Torres
#Data: 13/01/2026
#Versio: 2.1
#Crea una classe Rectangle amb els atributs amplada i alçada, i mètodes per calcular l'àrea i el perímetre
class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

    def area(self):
        return self.amplada * self.alçada

    def perimetre(self):
        return 2 * (self.amplada + self.alçada)
    
    def mostrar(self):
        print(f"Rectangle: Amplada = {self.amplada}, Alçada = {self.alçada}, Area = {self.area()}, Perímetre = {self.perimetre()}")



