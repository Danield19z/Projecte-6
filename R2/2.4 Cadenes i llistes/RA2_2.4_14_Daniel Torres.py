#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars.
llista_parells = []
llista_inpares = []
for i in range(10):
    numero = int(input("Introdueix un número: "))
    if numero % 2 == 0:
        llista_parells.append(numero)
    else:
        llista_inpares.append(numero)
print("Llista de números parells:", llista_parells)
print("Llista de números inpares:", llista_inpares)