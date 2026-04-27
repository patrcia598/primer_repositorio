dia= int(input("Ingresar número de dia: "))
mes=int(input("Ingresar número de mes: "))
anio = int(input("Ingresar número de año: "))
if mes < 1 or mes > 12:
    print("Fecha Invalida")
else:
    if mes ==2 :
        if (anio %4 == 0 and anio %100 != 0) or (anio %400 == 0 ):
         dias=29 
        else:
           dias = 28
    elif (mes==4 or mes ==6 or mes ==9 or mes==11):
        dias=30
    else:
       dias=31
if mes< 1 or mes>12:
   print("Fecha Inválida")
if dia<=0  or dia>= dias: 
   print("Fecha Inválida") 
else:
   print("Fecha Válida")

      
                                 
     
