#Programa fet per Daniel Torres
#Data: 13/01/2026
#Versio: 2.1
#Creacio d'una classe Estudiant amb atributs nom i nota, i un metode per comprovar si ha aprovat.
class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota
      
        if self.nota >= 5:
            print(f"{self.nom} ha aprovat. Nota: {self.nota}")





