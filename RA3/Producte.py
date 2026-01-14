#Programa fet per Daniel Torres
#Data: 13/01/2026
#Versio: 2.1
#Creacio d'una classe Producte amb atributs nom i preu, i un metode per mostrar la informacio del producte.
class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu_original = preu
        self.preu = preu

    def aplicar_descompte(self, percentatge):
        self.preu = self.preu_original * (1 - percentatge / 100)

    def mostrar_informacio(self):
        print(f"Producte: {self.nom}")
        print(f"Preu original: {self.preu_original:.2f} EUR")
        print(f"Preu amb descompte: {self.preu:.2f} EUR")


