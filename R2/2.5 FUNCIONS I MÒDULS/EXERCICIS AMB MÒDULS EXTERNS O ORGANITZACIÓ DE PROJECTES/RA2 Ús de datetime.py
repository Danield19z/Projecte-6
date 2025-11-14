#Programa fet per Daniel Torres
#Data: 07/11/2025
#Versio: 2.1
#Calcula quants dies falten per Nadal 
import datetime

ara = datetime.datetime.now()
print(ara)

nadal = datetime.datetime(ara.year, 12, 25)
print((nadal - ara).days, "dies per Nadal")
