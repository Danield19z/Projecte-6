#Programa fet per Daniel Torres
#Data: 21/01/2026
#Versio: 2.1
#Crea una classe que muestra la temperatura
class Termostat:
    def __init__(self):
        self.__temperatura = 20

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, t):
        if t >= 10 and t <= 30:
            self.__temperatura = t



