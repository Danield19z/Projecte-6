#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Comprova si diferents nombres són parells
def es_parell(numero):
    if numero % 2 == 0: 
        print("El número", numero, "és parell:", True)
    else:
        print("El número", numero, "és inparell:", False)
llista_parells = (int(input("Posa un nombre per comprovar si és parell: ")))
es_parell(llista_parells)

