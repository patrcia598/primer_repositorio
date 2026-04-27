saldo_actual= float(input("Ingresar importe saldo actual: "))
extraccion=float(input("Ingresar el importe a extraer: "))
if (extraccion < 0):
    print("Error: La extraccion no puede tener valores negativos")

else:

    if (extraccion % 1000 != 0):
        print("Extraccion Rechazada: La extracción debe ser multiplo de 1000")
    elif(extraccion> saldo_actual) :
        print("Extracción Rechazada: La extracción no puede superar el saldo actual")
    elif(extraccion> 100000):
        print("Extracción Rechazada: la extracción no puede ser superior a $100000")
    else:
        saldo_restante = saldo_actual - extraccion
        print("Extracción Aprobada")
        print("Saldo Actual en cuenta:",saldo_restante )    
               