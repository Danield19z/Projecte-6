#Programa fet per Daniel Torres
#Data: 21/01/2026
#Versio: 2.1
#Crea una clasee que lo que fa es verificar la contraseña i pots cambiar la contraseña
class Usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya

    def canviar_contrasenya(self, nova):
        if len(nova) >= 8:
            self.__contrasenya = nova
            return True, "Contrasenya canviada correctament"
        else:
            return False, "La contrasenya ha de tenir almenys 8 caràcters"

    def verificar_contrasenya(self, clau):
        return clau == self.__contrasenya




