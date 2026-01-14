#Programa fet per Daniel Torres
#Data: 13/01/2026
#Versio: 2.1
#Creacio d'una classe Cercle amb mètodes per calcular l'àrea i el perímetre.
class Cercle:
    tots = []

    def __init__(self, radi):
        self.radi = radi
        Cercle.tots.append(self) 
        
        if self.calcular_area() > 50:
            self.mostrar_informacio()

    def calcular_area(self):
        return 3.1416 * self.radi ** 2

    def calcular_perimetre(self):
        return 2 * 3.1416 * self.radi

    def mostrar_informacio(self):
        print(f"Cercle amb radi: {self.radi}")
        print(f"Àrea: {self.calcular_area()}")
        print(f"Perímetre: {self.calcular_perimetre()}")
        print()





