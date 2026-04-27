edad= int(input("Ingrese la edad: "))
dosis= int(input("Ingrese la cantidad de dosis: "))
if (edad < 18):
    print("Menor de edad")
    
else:
    print("Mayor de edad")
if (dosis == 0): 
        print("Estado: Sin vacunar")
elif(dosis ==1):
        print("Estado: Parcial") 
else:
        print("Estado: Completo")
if (edad < 18 and dosis >= 2):
      print("Apto para actividades escolares")   
elif(edad >= 18 and dosis >= 2): 
       print("Pase sanitaio habilitado") 
else:
      print("Debe completar esquema")       
