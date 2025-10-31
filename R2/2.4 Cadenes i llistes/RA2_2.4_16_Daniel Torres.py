#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Fes un programa que elimini els duplicats d'una llista
llistat = []
for i in range(5): 
    numero = int(input("Posa un número: "))
    llistat.append(numero)
llistat = list(set(llistat))
print("Llista sense duplicats:", llistat)
