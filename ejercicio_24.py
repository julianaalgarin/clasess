# Dependiendo del tipo de actividad, se aplica una retención: - Dependiente → 10% - Independiente → 15% - Empresario → 20%
# Solicita el tipo y el ingreso mensual y calcula el valor del impuesto. Valida que los ingresos
# sean positivos.


print("Tipo de actividad:")
print("1. Dependiente → 10% de retención")
print("2. Independiente → 15% de retención")
print("3. Empresario → 20% de retención")

tipo = int(input("Ingrese el número correspondiente al tipo de actividad (1-3): "))
ingreso = float(input("Ingrese su ingreso mensual: "))

if ingreso <= 0:
    print("Ingreso inválido. Debe ser un valor positivo.")
elif tipo == 1:
    impuesto = ingreso * 0.10
    print(f"Tipo: Dependiente")
    print(f"Impuesto a pagar: ${impuesto:}")
elif tipo == 2:
    impuesto = ingreso * 0.15
    print(f"Tipo: Independiente")
    print(f"Impuesto a pagar: ${impuesto:}")
elif tipo == 3:
    impuesto = ingreso * 0.20
    print(f"Tipo: Empresario")
    print(f"Impuesto a pagar: ${impuesto:}")
else:
    print("Tipo de actividad no válido.")
