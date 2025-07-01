# Se necesita construir un programa que indique si un número tiene exactamente tres cifras.
# Esto se cumple si el número está entre 100 y 999, o entre -999 y -100. Crea un algoritmo
# que lo detecte y lo indique con un mensaje. 

numero = int (input("Ingrese el número: "))

if (100 <= numero <= 999) or (-999 <= numero <= -100):
   print(f"el número tiene 3 cifras")
else:
   print("el número no tiene 3 cifras")   