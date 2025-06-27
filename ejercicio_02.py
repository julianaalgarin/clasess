# Un centro de salud recibe temperaturas tomadas de los pacientes al ingresar. Se debe
# desarrollar un algoritmo que reciba como entrada una temperatura (en grados Celsius) y
# muestre un mensaje indicando si el paciente presenta: - Hipotermia (menos de 36°C) - Temperatura normal (entre 36°C y 37.5°C inclusive) - Fiebre (más de 37.5°C)


temperatura = float (input("Ingrese la temperatura del paciente: "))
if temperatura < 36:
    print("El paciente tiene hipotermia")
elif 36 <= temperatura <= 37.5:
     print("El paciente tiene la temperatura normal")    
else:
    print ("El paciente tiene fiebre")     
