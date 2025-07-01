# Desarrolla un algoritmo que muestre un menú con las siguientes opciones:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# El usuario elige una opción e ingresa dos números. El programa debe realizar la operación
# seleccionada y mostrar el resultado. Si la división es por cero, indicar 'No se puede dividir
# por cero'. 

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int (input("Elige una opción (1-4): "))

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if opcion == 1:
    print("Resultado:", a + b)
elif opcion == 2:
    print("Resultado:", a - b)
elif opcion == 3:
    print("Resultado:", a * b)
elif opcion == 4:
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("No se puede dividir por cero")
else:
    print("Opción no válida")
