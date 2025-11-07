#Programa fet per Daniel Torres
#Data: 02/10/2025
#Versio: 2.1
#Demana a l'usuari una cadena de text i mostra-la invertida

text = input("Introdueix una cadena de text: ") #Demana a l'usuari una cadena de text
invertida = "" #Variable per invertir la cadena
for caracter in text: #Funcio per invertir la cadena
    invertida = caracter + invertida #Inverteix la cadena
print(invertida) #Mostra la cadena invertida

