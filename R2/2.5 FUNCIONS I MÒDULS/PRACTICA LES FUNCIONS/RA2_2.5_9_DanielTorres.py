#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Determina l'estat de diferents edats
def estat_persona(edat):
    if edat <= 12:
        return "Infantil"
    elif edat <= 25:
        return "Adult"
    elif edat <= 70:
        return "Abuelo"
print(estat_persona(12))
print(estat_persona(25))
print(estat_persona(70))