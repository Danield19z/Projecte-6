#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Demana a l'usuari un número enter i mostra la seva taula de multiplicar del 1 al 10
num = int(input("Introdueix un número enter: ")) #Variable num que emmagatzema el número introduït per l'usuari
for i in range(1, 11): #Variable i que recorre els números de l'1 al 10
    print(f"{num} x {i} = {num * i}") #Mostra la taula de multiplicar del número introduït per l'usuari