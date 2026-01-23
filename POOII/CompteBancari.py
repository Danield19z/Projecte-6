#Programa fet per Daniel Torres
#Data: 21/01/2026
#Versio: 2.1
#Creem la classe CompteBamcari amb el saldo privat i els metodes per ingressar, retirar i consultar el saldo
class CompteBancari:
    def __init__(self,saldo):
        self.__saldo=saldo #Privada
    
    def consulta_saldo(self):
        return self.__saldo
    
    def ingressa(self,quantitat):
        if quantitat > 0:
            self.__saldo == quantitat
    
    def retira_quantitat(self,quantitat,retirada):
        if quantitat - retirada >= 0:
            self.__saldo -= retirada
    
    def veure_quantitat(self):
        return self.__saldo
    
