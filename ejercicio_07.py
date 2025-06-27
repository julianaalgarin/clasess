# En una tienda de tecnología se aplican descuentos por el valor total de la compra: - Sin descuento si es menor a $100.000 - 5% si está entre $100.000 y $200.000 - 10% si supera los $200.000
# Crea un algoritmo que reciba el valor de la compra y muestre qué porcentaje de descuento
# aplica. 


valor_compra = float(input("Ingrese el valor de la compra: "))

if valor_compra <100000:
    print("No tienes descuento")

elif valor_compra >= 100000 and valor_compra <= 200000:
    print("Tienes descuento de 5%")  

elif valor_compra>200000:
     print("Tienes descuento del 10%") 

