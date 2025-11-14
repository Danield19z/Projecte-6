#Programa fet per Daniel Torres
#Data: 14/11/2025
#Versio: 2.1
#Escriu un programa que llegeixi i mostri el contingut per pantalla
fitxer = open("missatge.txt", "r")
contingut = fitxer.read()
fitxer.close
print(contingut)