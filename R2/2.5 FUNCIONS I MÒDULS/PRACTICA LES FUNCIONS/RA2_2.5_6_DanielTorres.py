#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Defineix multiplica_tot(*nombres)
def  multiplica_tot(*nombres):
    resultat = 1
    for nombre in nombres:
        resultat *= nombre
    print("La multiplicació de els números és:", resultat)
multiplica_tot(2, 3, 4)
multiplica_tot(5, 10)
