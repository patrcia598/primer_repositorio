horas = int(input("Ingrese la cantidad de años de antiguedad:"))
vehiculo  =input("Ingresar tipo vehiculo (moto/auto): ")
horario = int(input("el horario que ingresa(0 a 24):"))

if (horas<= 2):
    monto = horas * 2000
elif (horas<= 5):
     monto = horas * 1200 
else:
     monto = horas * 1000
if (vehiculo == "moto" ) :
     monto = monto * 0.7
if (horario >= 22):
     monto= monto * 0.9
print("Total a pagar: $", monto)             

