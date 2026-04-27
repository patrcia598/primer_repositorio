edad= int(input("Ingrese la edad: "))
monto_compra = float(input("Ingrese el monto de compra: "))
if (edad < 18):
    print("Menor de edad")
    
else:
    print("Mayor de edad")
if  (monto_compra >= 10000):
    print("Compra: Alta") 
elif(monto_compra >= 5000):
    print("Compra: Media") 
else:
    print("Compra: Baja")
if (edad< 18 and monto_compra >= 5000) :
    print("Descuento del 10%")  
elif(edad >= 18 and monto_compra >= 10000): 
       print("Descuento del 15%")
else:
      print("Sin Descuento ")                   
