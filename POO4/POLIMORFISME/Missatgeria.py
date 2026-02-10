#Fet per Daniel
#10/02/2026
#Crea classes i subclasses de missatgers i mostra polimorfisme: cada missatger envia el missatge a la seva manera
class Missatger:
    def enviar(self, missatge):
        return f"Missatge genèric: {missatge}"

class Email(Missatger):
    def enviar(self, missatge):
        return f"Enviant per Email: {missatge}"

class SMS(Missatger):
    def enviar(self, missatge):
        return f"Enviant per SMS: {missatge}"

class WhatsApp(Missatger):
    def enviar(self, missatge):
        return f"Enviant per WhatsApp: {missatge}"

email = Email()
sms = SMS()
whatsapp = WhatsApp()
print(email.enviar("Hola!"))
print(sms.enviar("Hola!"))
print(whatsapp.enviar("Hola!"))
