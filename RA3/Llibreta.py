#Programa fet per Daniel Torres
#Data: 13/01/2026
#Versio: 2.1
#Creació d'una classe Llibre amb atributs i mètode per mostrar informació
class Llibre:
    def __init__(self, titul, autor, any):
        self.titul = titul
        self.autor = autor
        self.any = any

    def mostrar_informacio(self):
        print(f"Títol: {self.titul}, Autor: {self.autor}, Any: {self.any}")
 
class Biblioteca:
    def __init__(self):
        self.llibres = []  

    def afegir_llibre(self, llibre):
        self.llibres.append(llibre)

    def mostrar_tots(self):
        if not self.llibres:
            print("No hi ha llibres a la biblioteca.")
        else:
            for llibre in self.llibres:
                llibre.mostrar_informacio()

