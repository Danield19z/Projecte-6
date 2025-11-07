#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Conversió de temperatures
import conversions

c = int(input("Temperatura en Celsius: "))
print("En Fahrenheit:", conversions.celsius_a_fahrenheit(c))

f = int(input("Temperatura en Fahrenheit: "))
print("En Celsius:", conversions.fahrenheit_a_celsius(f))
