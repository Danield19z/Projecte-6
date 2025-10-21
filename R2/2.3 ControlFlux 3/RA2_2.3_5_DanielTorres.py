#Programa fet per Daniel Torres
#Data: 17/10/2023
#Versio: 2.1
#Demana a l'usuari un nombre enter i imprimeix tots els nombres primers des de 2 fins a aquest nombre
try:
    num = int(input("Introdueix un nombre enter positiu: "))
    if num < 2:
        print("Si us plau, introdueix un nombre enter major o igual a 2.")
    else:
        print(f"Nombres primers des de 2 fins a {num}:")
        for n in range(2, num + 1):
            es_primer = True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    es_primer = False
                    break
            if es_primer:
                print(n, end=' ')
        print()  # Nova línia després de la llista de nombres primers
except ValueError:
    print("Entrada no vàlida. Si us plau, introdueix un nombre enter.")