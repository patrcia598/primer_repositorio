#ingresar datos
cantidad_entradas =float(input("Ingrese cantidad entradas compradas: "))
#Calcular monto sin descuento
monto1 = cantidad_entradas * 3500
#calcular descuento
descuento = monto1 * 0.20
#calcular monto final
monto_final1 = monto1 - descuento
print("Monto final a pagar: $" ,monto_final1)