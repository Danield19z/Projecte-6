#Programa fet per Daniel Torres
#Data: 13/01/2026
#Versio: 2.1
#Creacio d'una classe Animal i una subclasse Gos que sobreescriu el metode fer_soroll.
class Animal:
    def __init__(self, nom, raça):
        self.nom = nom
        self.raça = raça

    def fer_soroll(self):
        print("L'animal fa un soroll")

    def descriure(self):
        print(f"Nom: {self.nom}, Raça: {self.raça}")

    def mostrar_informacio(self):
        self.descriure()
        self.fer_soroll()

class Gos(Animal):
    def fer_soroll(self):
        print("Bup bup!")
