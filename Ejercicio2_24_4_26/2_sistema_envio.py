try:
    peso=float(input("Ingresar peso del paquete: "))
    destino=input("Ingresar destino: ")
    cliente=input("Ingresar tipo de cliente: ")
    if (peso<= 5):
        importe= 2000
    elif(peso<=20):
        importe=5000
        
    else:
        importe = 10000 
    if (destino == "interior") :
        importe= importe * 1.15
    if (cliente == "premium" ):
        importe= importe * 0.8
    print("Costo total envio: $" ,importe)
except:
    print("Datos invalidos")

     
