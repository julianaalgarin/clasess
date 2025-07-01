# Crea un programa que lea un número del 1 al 12 y muestre el nombre del mes
# correspondiente. Por ejemplo, 1 → 'Enero', 2 → 'Febrero', etc. Si se ingresa un número
# inválido, mostrar 'Mes no válido'. 

numero = int (input("Ingresa un número: "))

if numero == 1:
    print("Enero")
elif numero == 2: 
    print("Febrero")
elif numero == 3:
    print ("Marzo")
elif numero == 4:
    print("Abril") 
elif numero == 5:
    print ("Mayo") 
elif numero == 6:
    print("Junio")  
elif numero == 7:
    print ("Julio")  
elif numero == 8:
    print ("Agosto") 
elif numero == 9:
    print ("Septiembre")     
elif numero == 10:
    print ("Octubre") 
elif numero == 11:
    print ("Noviembre") 
elif numero == 12:
    print ("Diciembre")                     
else:
    print("ERROR, EL MES NO ES VÁLIDO")       
