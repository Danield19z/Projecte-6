#Fet per Daniel Torres
#05/11/2021
#Descomposició horària d'un nombre de segons donat
segons = int(input("Posa el nombre de segons: "))
print(segons//3600, (segons%3600)//60, segons%60)
