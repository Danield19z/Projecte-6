#Programa fet per Daniel Torres
#Data: 02/10/2025
#Versio: 2.1
#Demana a l'usuari un número enter i mostra la seva taula de multiplicar del 1 al 10
from asyncio import sleep #Variable per fer pauses en el programa
nom =int(input("Introdueix un número enter: ")) #Variable per demanar a l'usuari un número enter
for i in(1,2,3,4,5,6,7,8,9,10): #Funcio per fer la taula de multiplicar del 1 al 10
    sleep(0.25) #Funcio per fer una pausa de 0.25 segons entre cada línia
    print(i,"x",nom,"=",nom * i) #Mostra la taula de multiplicar del número introduït per l'usuari