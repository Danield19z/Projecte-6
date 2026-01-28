#Programa fet per Daniel Torres
#Data: 28/01/2026
#Versio: 2.1
#Crea una classe CarretCompra que tingui un mètode calcular_total_amb_descompte.
class Descompte20:
    def aplicar_descompte(self, preu):
        return preu * 0.2

class CarretCompra:
    def __init__(self,total):
        self.total=total
    
    def calcular_total_amb_descompte(self, preu):
        return self.total.aplicar_descompte(preu)

descompte = CarretCompra(Descompte20())
print(descompte.calcular_total_amb_descompte(100))