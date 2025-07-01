# Un parqueadero cobra según el tipo de vehículo: - Carro → $5.000/hora - Moto → $2.000/hora - Bicicleta → $500/hora
# Diseña un algoritmo que reciba el tipo de vehículo y el número de horas y calcule el total a pagar.


print("1. Carro → $5.000/hora")
print("2. Moto → $2.000/hora")
print("3. Bicicleta → $500/hora")

opcion = int(input("Ingrese una opción (1-3): "))
horas = float(input("Ingrese el número de horas que estuvo el vehículo: "))

if opcion == 1:
    tarifa = 5000
    print("Carro - $5.000/hora")
    total = tarifa * horas
    print(f"Total a pagar: ${total:}")
elif opcion == 2:
    tarifa = 2000
    print("Moto - $2.000/hora")
    total = tarifa * horas
    print(f"Total a pagar: ${total:}")
elif opcion == 3:
    tarifa = 500
    print("Bicicleta - $500/hora")
    total = tarifa * horas
    print(f"Total a pagar: ${total:}")
else:
    print("Opción no válida")

    
