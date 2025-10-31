#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Demana a l'usuari 5 paraules i emmagatzema-les en una llista.
llista_paraules = []
for i in range(5):
    paraula = input("Introdueix una paraula: ")
    llista_paraules.append(paraula)
print("Llista de paraules:", llista_paraules)