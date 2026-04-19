#ingresar datos
cantidad_prendas =float(input("Ingrese cantidad prendas compradas: "))
#Calcular monto sin descuento
monto = cantidad_prendas * 8000
#calcular descuento
descuento = monto * 0.25
#calcular monto final
monto_final = monto - descuento
print("Monto final a pagar: $" ,monto_final)