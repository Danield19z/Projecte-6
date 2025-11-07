#Programa fet per Daniel Torres
#Data: 02/10/2025
#Versio: 2.1
#Te diu si son vocals o consonants
lletra = input("Introdueix una lletra: ") #Variable que demana una lletra
if(lletra in ['a','e','i','o','u']): #Condicio que comprova si la lletra es una vocal
              print("La lletra es una vocal") #Missatge que surt si es una vocal
else:
              print("La lletra es una consonant") #Missatge que surt si es una consonant