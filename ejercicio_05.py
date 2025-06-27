# Un sistema digital restringido solicita al usuario ingresar un nombre de usuario y una
# contraseña. Si ambos coinciden exactamente con los valores esperados ('admin' y '1234'), se
# debe mostrar 'Acceso concedido'. En caso contrario, mostrar 'Acceso denegado'. Crea el
# algoritmo para esta validación.


username = (input("Ingrese su nombre de usuario: "))
password = (input("Ingrese su contraseña: "))

if username == "admin" and password == "1234":
    print ("Acceso concedido")
else:
    print ("Acceso denegado")    