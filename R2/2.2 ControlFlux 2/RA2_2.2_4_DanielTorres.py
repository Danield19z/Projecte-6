#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Genera un número aleatori entre 1 i 100. Demana a l'usuari que endevini el número, donant pistes de "massa alt" o "massa baix" fins que l'encerti
import random #Variable per generar números aleatoris

secret = random.randint(1, 100) #Variable per generar un número aleatori entre 1 i 100

for _ in range(1000000):  # Funcio per limitar el nombre d'intents
    numero = int(input("Endevina el número: ")) #Variable per demanar a l'usuari que endevini el número
    if numero < secret: #Variable per donar pistes a l'usuari
        print("Massa baix!") #Mostra el missatge en pantalla si es massa baix
    elif numero > secret: #
        print("Massa alt!") #Mostra el missatge en pantalla si es massa alt
    else:
        print("Has encertat!")  #Mostra el missatge en pantalla si l'usuari encerta el número
        break #Funcio per acabar el programa si l'usuari encerta el número
