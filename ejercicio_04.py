# Una campaña de donación requiere filtrar a los posibles donantes. Para ser apto, la persona
# debe tener entre 18 y 65 años y pesar al menos 50 kg. Escribe un algoritmo que reciba la
# edad y el peso de una persona, y determine si está apta o no para donar sangre, mostrando
# un mensaje adecuado.

edad = int(input("Ingrese la edad del donante: "))
peso = float(input("Ingrese el peso del donante: "))

if edad < 18:
    print("La edad del paciente no es apta para la donación")
elif edad > 65:
    print("La edad del paciente no es apta para la donación")
else:
    print("La edad del paciente es apta para la donación")

if peso >= 50:
    print("El peso del paciente es apto para la donación")
else:
    print("El peso del paciente no es apto para la donación")

     