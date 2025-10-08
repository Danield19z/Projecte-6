#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Demana a l'usuari una cadena de text i mostra-la invertida
for i in range(1): #Funció per repetir el codi
    text = input("Introdueix una cadena de text: ") #Variable on s'emmagatzema la cadena de text
    text_invertit = text[::-1] #Variable on s'emmagatzema la cadena de text invertida
    print("Cadena invertida:", text_invertit) #Mostra en pantalla la cadena de text invertida