#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Demana a l'usuari un número enter positiu i determina si és un nombre primer o no

num = int(input("Introdueix un número enter positiu: ")) #Variable per emmagatzemar el número introduït per l'usuari
if num < 2: 
    print(num, "no és un nombre primer.") 
else: 
    primer = True  # Suposem que és primer
   
    for i in range(2, num):
        if num % i == 0:  # Si trobem algun divisor
            primer = False
            break  # Parem el bucle, ja sabem que no és primer
    
    if primer:
        print(num, "és un nombre primer.") #Mostra el missatge en pantalla si el número és primer
    else:
        print(num, "no és un nombre primer.") #Mostra el missatge en pantalla si el número no és primer
