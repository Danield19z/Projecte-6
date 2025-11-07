#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Determina l'estat de diferents edats
edat = int(input("posa edat: "))
def estat_persona(edat):
    if edat <= 12:
        return "Infantil"
    elif edat >= 18:
        return "Adult"
    elif edat >= 70:
        return "Abuelo"
print (estat_persona(edat)) 
