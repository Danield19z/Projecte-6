#Programa fet per Daniel Torres
#Data: 21/01/2026
#Versio: 2.1
#Crea una clase rellotge en el format 00:00
class Rellotge:
    def __init__(self, hores=0):
        self.set_hores(hores)

    def set_hores(self, valor):
        if 0 <= valor <= 23:
            self.__hores = valor
        else:
            raise ValueError("Les hores han d'estar entre 0 i 23")

    def get_hores(self):
        return self.__hores

    def mostrar(self):
        return f"{self.__hores:02d}:00"


