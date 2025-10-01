#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Lo que fa es dir quin numero es mes gran de tres numeros que li dones
num1 = int(input("Introdueix el primer numero: ")) #Variable que te demana el primer numero
num2 = int(input("Introdueix el segon numero: ")) #Variable que te demana el segon numero
num3 = int(input("Introdueix el tercer numero: ")) #Variable que te demana el tercer numero
if num1 >= num2 and num1 >= num3: #Condicio que comprova si el primer numero es el mes gran
    print("El numero mes gran es: ", num1) #Variable que et diu quin numero es el mes gran
elif num2 >= num1 and num2 >= num3: #Condicio que comprova si el segon numero es el mes gran
    print("El numero mes gran es: ", num2) #Variable que et diu quin numero es el mes gran
else:
    print("El numero mes gran es: ", num3) #Variable que et diu quin numero es el mes gran
    