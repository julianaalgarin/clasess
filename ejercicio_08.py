# Una institución educativa aprueba a un estudiante si cumple dos condiciones: una nota final
# igual o superior a 3.0 y una asistencia igual o superior al 80%. Escribe un algoritmo que
# reciba estos dos datos y determine si el estudiante aprueba o reprueba.


notas = float (input("Ingrese la nota del estudiante: "))
asistencias = int(input("Ingrese la cantidad de asistencias del estudiante: "))

if notas >= 3:
    print("El estudiante tiene la nota necesaria para aprobar")
else:
    print("El estudiante no tiene la nota necesaria para aprobar")    

if asistencias >= 80:
    print("El estudiante tiene la asistencia necesaria")
else:
    print("El estudiante no tiene la asistencia necesaria para aprobar")  
      
if notas >= 3 and asistencias >= 80:
    print("El estudiante APRUEBA")
else:
    print("El estudiante REPRUEBA")    