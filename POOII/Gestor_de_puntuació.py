#Programa fet per Daniel Torres
#Data: 21/01/2026
#Versio: 2.1
#Crea una classe que apunta els punts
class Joc:
    def __init__(self):
        self.__puntuacio = 0

    def sumar_punts(self, punts):
        self.__puntuacio += punts

    def reiniciar(self):
        self.__puntuacio = 0

    def get_puntuacio(self):
        return self.__puntuacio


