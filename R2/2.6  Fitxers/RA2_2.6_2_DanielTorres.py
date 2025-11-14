#Programa fet per Daniel Torres
#Data: 14/11/2025
#Versio: 2.1
#programa que escrigui les següents 3 línies en un fitxer
fitxer = open("missatge.txt", "w") 
contingut = fitxer.read()           
fitxer.close()                      
print(contingut)  