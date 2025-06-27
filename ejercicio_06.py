# Un proveedor de servicios de Internet desea implementar una herramienta que clasifique el
# servicio que tiene un usuario. Se debe ingresar la velocidad del plan en Mbps y mostrar:
# - 'Muy lenta' si es menor a 10 Mbps - 'Aceptable' si es entre 10 y 30 Mbps - 'Buena' si es entre 31 y 100 Mbps - 'Alta velocidad' si es mayor a 100 Mbps

speedtest = int(input("Ingrese la velocidad de su plan en Mbps: "))

if speedtest < 10:
    print("Su velocidad es muy lenta")

elif speedtest >= 10 and speedtest <= 30:

    print("Su velocidad es aceptable")

elif speedtest >= 31 and speedtest <= 100:

    print("Su velocidad es buena")
    
else:
    print("Su velocidad es alta")