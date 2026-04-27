try:
    antiguedad = int(input("Ingrese la cantidad de años de antiguedad:"))
    sueldo  =float(input("Ingresar monto sueldo: "))
    if (antiguedad < 0 or sueldo < 0):
        print("El valor ingresado debe ser mayor a cero")
    if (antiguedad >= 10):
        sueldo= sueldo * 1.10
    elif(antiguedad >= 5):
        sueldo = sueldo * 1.07
    else:
        sueldo = 1.05
    if (sueldo < 500000 ):
        sueldo = sueldo * 1.03
    print("Sueldo Final a Cobrar: $", sueldo)
except:
    print("Datos invalidos")               