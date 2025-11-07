#Programa fet per Daniel Torres
#Data: 02/10/2025
#Versio: 2.1
#Demana a l'usuari una frase i compta quantes vocals conté
frase = input("Introdueix una frase: ") #Variable per guardar la frase
vocals = "aeiouAEIOU" #Variable per guardar les vocals
comptador = 0 #Variable per comptar les vocals
for lletra in frase: #Funció per recórrer la frase
    if lletra in vocals: #Condició per comprovar si la lletra és una vocal
        comptador += 1 #Si és una vocal, suma 1 al comptador
print("La frase conté", comptador, "vocals.") #Mostra el resultat per pantalla