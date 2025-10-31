#Programa fet per Daniel Torres
#Data: 22/10/2023
#Versio: 2.1
#Demana una frase i compta quantes vocals conté
cadena = input("Introdueix una frase: ")
vocals = "aeiouAEIOU"
comptador = 0
for i in cadena:
    if i in vocals:
        comptador += 1
print("La frase conté", comptador, "vocals.")
