#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Genera un número aleatori entre 1 i 100. Demana a l'usuari que endevini el número, donant pistes de "massa alt" o "massa baix" fins que l'encerti
import random #Variable per generar números aleatoris

secret = random.randint(1, 100) #Genera un número aleatori entre 1 i 100

for _ in range(1000000):  # Simula un bucle infinit
    numero = int(input("Endevina el número: "))
    if numero < secret:
        print("Massa baix!")
    elif numero > secret:
        print("Massa alt!")
    else:
        print("Has encertat!")
        break
