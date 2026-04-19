#ingresar datos
precio =float(input("Ingrese el precio base del prodcto: "))
#Calcular IVA
iva = precio * 0.21
#calcular precio mas iva
precio_iva = precio + iva
print("Precio final con IVA: $" ,precio_iva)