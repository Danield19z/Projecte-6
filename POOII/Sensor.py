#Programa fet per Daniel Torres
#Data: 21/01/2026
#Versio: 2.1
#Crea un sensor para controlar el limite de valor
class Sensor:
    def __init__(self):
        self.__valor = 0

    def llegir_valor(self):
        return self.__valor

    def modificar_valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor


