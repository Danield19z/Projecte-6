#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Filtra nombres parells de diverses llistes
def filtra_parells(llista):
    parells = ()
    for numero in llista:
        if numero % 2 == 0:
            parells += (numero,)
    print("Nombres parells:", parells)
filtra_parells([1, 2, 3, 4, 5, 6])
filtra_parells([10, 15, 20, 25, 30])
