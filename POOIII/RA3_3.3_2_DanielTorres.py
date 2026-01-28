#Programa fet per Daniel Torres
#Data: 28/01/2026
#Versio: 2.1
#Creacio d'una classe per notificar per email la confirmacio d'una comanda
class EmailNotificador:
    def enviar(self, missatge):
        print(f"Enviant email amb el missatge: {missatge}")
    
class comanda:
    def __init__(self,client,emailnotificador):
        self.client=client
        self.notificador= emailnotificador
        
    def confirmar(self):
        print(f"Comanda confirmada per {self.client}")
        self.notificador.enviar(f"Hola {self.client}, la teva comanda ha estat confirmada.")

servei = EmailNotificador()
usuari = comanda("Daniel Torres", servei)
usuari.confirmar()