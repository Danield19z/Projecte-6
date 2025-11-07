#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Crea una carpeta utilitats amb
import moneda 
import temps 

segons = int(input("Segons: "))
print(temps.segons_a_minuts(segons), "minuts")
print(temps.segons_a_hores(segons), "hores")

euros = float(input("Euros: "))
print(moneda.euros_a_dolars(euros), "dòlars")

dolars = float(input("Dòlars: "))
print(moneda.dolars_a_euros(dolars), "euros")
