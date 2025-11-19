#Programa fet per Daniel Torres
#Data: 14/11/2025
#Versio: 2.1
#Intenta obrir un fitxer en mode lectura i si no estalo crea
try:
    fitxer = open("nou_fitxer.txt", "r")
    print(fitxer.read())
    fitxer.close()
except FileNotFoundError:
    fitxer = open("nou_fitxer.txt", "w")
    fitxer.write("Fitxer creat automàticament\n")
    fitxer.close()
    print("Fitxer creat automàticament.")
