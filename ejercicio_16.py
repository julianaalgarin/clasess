﻿# Diseña un algoritmo que reciba un número del 1 al 7 y muestre el día correspondiente de la
# semana. Si se ingresa un número fuera de ese rango, mostrar un mensaje de error. Usa una
# estructura ‘según’ o ‘switch’.

numero = int (input("Ingresa un número: "))

match numero:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3: 
        print("Miércoles")  
    case 4:
        print("Jueves") 
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")      
    case 7:
        print("Domingo")
    case _:
        print("ERROR, EL NÚMERO NO ES VÁLIDO")    