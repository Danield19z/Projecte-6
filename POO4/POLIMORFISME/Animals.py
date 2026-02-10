#Fet per Daniel
#10/02/2026
#Defineix una classe base Animal amb un mètode genèric fer_soroll(), dues subclasses Gat i Vaca
class Animal:
    def fer_soroll(self):
        return "Algú fa un soroll..."  

class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"

def reproduir_soroll(animal):
    print(animal.fer_soroll())


gat = Gat()
vaca = Vaca()

reproduir_soroll(gat)   
reproduir_soroll(vaca)  
