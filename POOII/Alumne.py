#Programa fet per Daniel Torres
#Data: 21/01/2026
#Versio: 2.1
#Crea una classe que diu la edat i no acepta numeros negativos
class Alumne:
    def __init__(self, edat=None):
        self.__edat = edat
        self.set_edat(edat)

    def set_edat(self, edat):
        if edat >= 0:
            self.__edat = edat
        else:
            print(f"Avís: l'edat és negativa i no s'ha canviat.")

    def get_edat(self):
        return self.__edat







