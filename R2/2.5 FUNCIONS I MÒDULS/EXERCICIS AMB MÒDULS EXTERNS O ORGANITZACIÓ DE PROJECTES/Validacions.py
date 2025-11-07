#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Crea validacions.py amb funcions
def es_email_valid(email):
    return "@" in email and "." in email

def es_telefon_valid(telefon):
    return telefon.isdigit()
