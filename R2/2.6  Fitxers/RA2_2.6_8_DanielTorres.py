#Programa fet per Daniel Torres
#Data: 14/11/2025
#Versio: 2.1
#un programa que llegeixi cada línia i la transformi en enter
fitxer = open("nombres.txt", "r")
for linia in fitxer:
    try:
        print(int(linia))  
    except ValueError:
        print("Línia no vàlida:", linia.strip())
fitxer.close()
