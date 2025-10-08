#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Genera un número aleatori entre 1 i 100. Demana a l'usuari que endevini el número, donant pistes de "massa alt" o "massa baix" fins que l'encerti
import random #Importa la llibreria random per generar números aleatoris

secret = random.randint(1, 100)#Genera un número aleatori entre 1 i 100

numero = 0 #Variable per guardar el número introduït per l'usuari
while numero != secret: #Bucle que es repeteix fins que l'usuari encerti el número
    numero = int(input("Endevina el número: ")) #Demana a l'usuari que introdueixi un número
    if numero < secret: #Funció per donar pistes a l'usuari
        print("Massa baix!") #Missatge que s'imprimeix quan el número és massa baix
    elif numero > secret: #Funció per donar pistes a l'usuari
        print("Massa alt!") #Missatge que s'imprimeix quan el número és massa alt
    else:
        print("Has encertat!") #Missatge que s'imprimeix quan l'usuari encerta el número


