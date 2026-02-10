#Fet per Daniel
#10/02/2026
# Crea figures (quadrat i cercle) que calculen la seva àrea amb herència
import math
class Figura:
    def area(self):
        print("Àrea no definida")

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        return self.costat ** 2

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * self.radi ** 2


q = Quadrat(5)
c = Cercle(3)
print("Àrea del quadrat:", q.area())   
print("Àrea del cercle:", c.area())    
