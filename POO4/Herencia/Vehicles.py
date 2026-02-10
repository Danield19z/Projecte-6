#Fet per Daniel
#10/02/2026
#Crea un cotxe amb una marca, hereta el comportament del vehicle i pot arrencar i tocar el clàxon.
class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print("El vehicle està arrencant")


class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")

cotxe = Cotxe("Toyota")
cotxe.arrencar()
cotxe.tocar_claxon()