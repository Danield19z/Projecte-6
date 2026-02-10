#Fet per Daniel
#10/02/2026
#Crea classes i subclasses de vehicles i mostra polimorfisme: cada vehicle es mou a la seva manera
class Vehicle:
    def moure(self):
        return "El vehicle es mou"

class Cotxe(Vehicle):
    def moure(self):
        return "El cotxe condueix per la carretera"

class Bicicleta(Vehicle):
    def moure(self):
        return "La bicicleta pedala per la pista"

class Barca(Vehicle):
    def moure(self):
        return "La barca navega pel riu"

cotxe = Cotxe()
bicicleta = Bicicleta()
barca = Barca()
print(cotxe.moure())
print(bicicleta.moure())
print(barca.moure())
