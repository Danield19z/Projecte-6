#Programa fet per Daniel Torres
#Data: 14/11/2025
#Versio: 2.1
#Llegeix un fitxer i mostra quantes línies té
fitxer = open("sortida.txt", "r")  
linies = fitxer.readlines()         
print("El fitxer té", len(linies), "línies.") 
fitxer.close()                      
