# Para garantizar la seguridad, una montaña rusa permite el ingreso solo a personas que
# tengan una edad igual o mayor a 12 años y una estatura igual o mayor a 1.40 metros. Crea
# un algoritmo que reciba la edad y estatura de una persona y determine si puede subir o no a
# la atracción. 

edad = int(input("Ingresa la edad de la persona: "))
estatura = float (input("Ingresa la estatura de la persona: " ))

if edad >= 12:
   print("La edad está en el rango permitido")
else:
   print("La edad no está entre el rango permitido")   

if estatura >= 1.40:
    print("La estatura está en el rango permitido")
else:
   print("La estatura no está en el rango permitido")    
