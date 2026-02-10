#Fet per Daniel
#10/02/2026
#Crea animals que parlen amb sons diferents mitjançant herència.
class Animal:
    def parlar(self):
        print("L'animal fa un so")

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")


class Gat(Animal):
    def parlar(self):
        print("Miau!")

a = Animal()
b = Gat()
c = Gos()
a.parlar()
b.parlar()
c.parlar()

