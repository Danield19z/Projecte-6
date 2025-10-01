#Programa fet per Daniel Torres
#Data: 02/10/2023
#Versio: 2.1
#Demana a l'usuari una frase i compta quantes vocals conté
frase = input("Introdueix una frase: ")
vocals = "aeiouAEIOU"
comptador = 0
for lletra in frase:
    if lletra in vocals:
        comptador += 1
print("La frase conté", comptador, "vocals.")