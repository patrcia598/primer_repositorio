edad= int(input("Ingrese la edad alumno: "))
asistencia = float(input("Ingrese el porcentaje de asistencia (de 0 a 100): "))
if (edad < 18):
    print("Menor de edad")
else:
    print("Mayor de edad")
    
if (asistencia >= 90):
      print("Asistencia: Excelente") 
elif(asistencia >= 75) :
      print("Asistencia: Buena")  
elif (asistencia >= 60):
      print("Asistencia: Regular") 
else:
      print("Asistencia: Mala")          
if (edad >=18 and asistencia >= 90):
      print(" Promocion directa")
elif (edad <18 and asistencia >= 75) or (edad >= 18 and asistencia >=75):
       print("Regulariza la materia")  

else:
       print("Libre por inasistencia") 