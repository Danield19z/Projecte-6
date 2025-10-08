#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Mostra els primers 10 termes de la seqüència de Fibonacci
num = int(input("Introdueix un número enter positiu: ")) #Variable per emmagatzemar el número introduït per l'usuari

for i in range(2, num): #Variable per recórrer els nombres des de 2 fins a num-1
    if num % i == 0: #Funcio que diu que si el número és divisible per algun altre número
        print(num, "no és un nombre primer.")
        break
else: #Funcio que diu que si no s'ha trencat el bucle
    if num > 1:
        print(num, "és un nombre primer.") #Mostra el missatge en pantalla si el número és primer
    else:
        print(num, "no és un nombre primer.") #Mostra el missatge en pantalla si el número no és primer
