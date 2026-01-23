#Programa fet per Daniel Torres
#Data: 21/01/2026
#Versio: 2.1
#Fer a classe per revisar el correu electronic d'un usuari
class CompteUsuari:
    def __init__(self, email=""):
        self.__email = ""
        self.set_email(email)

    def set_email(self, email):
        if "@" in email and "." in email:
            self.__email = email
        else:
            print(f"Avís: l'email '{email}' no és vàlid i no s'ha canviat.")

    def get_email(self):
        return self.__email



