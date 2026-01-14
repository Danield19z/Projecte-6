#Programa fet per Daniel Torres
#Data: 13/01/2026
#Versio: 2.1
#Creacio d'una classe Persona amb atributs nom i edat, i un metode per presentar-se.
class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
        
        if self.edat > 30:
            self.presentar_se()

    def presentar_se(self):
        print(f"Hola, soc {self.nom} i tinc {self.edat} anys")

