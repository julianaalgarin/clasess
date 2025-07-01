# Diseña un algoritmo que reciba un número del 1 al 7 y muestre el día correspondiente de la
# semana. Si se ingresa un número fuera de ese rango, mostrar un mensaje de error. Usa una
# estructura ‘según’ o ‘switch’.

numero = int (input("Ingresa un número: "))

if numero == 1:
    print("Lunes")
elif numero == 2: 
    print("Martes")
elif numero == 3:
    print ("Miércoles")
elif numero == 4:
    print("Jueves") 
elif numero == 5:
    print ("Viernes") 
elif numero == 6:
    print("Sábado")  
elif numero == 7:
    print ("Domingo")  
else:
    print("ERROR, EL NÚMERO NO ES VÁLIDO")                 