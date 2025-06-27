# Un sistema de reservas permite elegir entre 3 tipos de evento:
# 1. Cine ($20.000)
# 2. Teatro ($35.000)
# 3. Concierto ($50.000)
# Luego debe ingresar la cantidad de entradas deseadas. Si el total supera los $100.000, se
# aplica un 10% de descuento. Calcula el total a pagar.

print("1 - 'Cine' ($20.000)")
print("2 - 'Teatro' ($35.000)")
print("3 - 'Concierto' ($50.000)")

boletas = int(input("Selecciona las boletas que deseas: "))

if boletas == 1:
    print("1 - 'Cine' ($20.000)")
    precio = 20000
elif boletas == 2:
    print("2 - 'Teatro' ($35.000)")
    precio = 35000
elif boletas == 3:
    print("3 - 'Concierto' ($50.000)")
    precio = 50000
else:
    print("No es una opción válida")
    exit()

entradas = int(input("Ingresa la cantidad de entradas que deseas: "))

total = precio * entradas

if total > 100000:
    total *= 0.9
    print("Tienes un descuento del 10%")
else:
    print("No tienes descuento")

print(f"Total a pagar: ${total}")


