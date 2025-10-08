#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Demana a l'usuari un número enter positiu i determina si és un nombre primer o no
num = int(input("Introdueix un número enter positiu: ")) #Variable per emmagatzemar el número introduït per l'usuari
if num > 2: #Variable que diu que si el número és més gran que 2
    for i in (2, num): #Variable per recórrer els nombres des de 2 fins a num-1
        if num % i == 0: #Funcio que diu que si el número és divisible per algun altre número
            print("El número no és primer") #Mostra el missatge en pantalla si el número no és primer
            break #Funcio que trenca el bucle
    else: #Funcio que diu que si no s'ha trencat el bucle
        print("El número és primer") #Mostra el missatge en pantalla si el número és primer
elif num == 2: #Variable que diu que si el número és igual a 2
    print("El número és primer") #Mostra el missatge en pantalla si el número és primer