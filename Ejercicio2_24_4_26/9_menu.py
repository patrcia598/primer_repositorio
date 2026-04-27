#Asignamos precios
hamburguesas = 10000
pizza = 15000
ensalada = 8000
empanadas = 3000
gaseosa= 7000
agua = 4000
#mostrar menu
print("MENU: ")
print("COMIDAS: ")
print("hamburguesas...................$ 10.000.-")
print("pizza..........................$ 15.000.-")
print("ensalada......................$  8.000.-")
print("empanadas......................$  3.000.-")
print("BEBIDAS:")
print("gaseosa........................$  7.000.-")
print("agua...........................$  4.000.-")
#Ingreso usuario

opcion1 =input("Ingrese la comida seleccionada: ").lower()
opcion2=input("Ingrese la bebida seleccionada: ").lower()
#damos valor numerico a los string ingresados
if(opcion1 =="hamburguesas"):
    precio1 = hamburguesas
elif(opcion1 == "pizza"):
      precio1 = pizza 
elif(opcion1 == "ensalada"): 
      precio1 = ensalada
elif (opcion1== "empanadas"): 
       precio1 = empanadas
else:
     precio1 = 0 

if(opcion2 == "gaseosa"):
     precio2 = gaseosa  
elif(opcion2 == "agua"):  
    precio2 = agua 
else:
     precio2 = 0                        
total = precio1 + precio2
#Reglas
if (opcion1 =="ensalada" and opcion2=="agua"):
    total = total * 0.8
elif (opcion1== "pizza" and opcion2 =="gaseosa"):
    total= total * 1.10
#Muestra precio final
print(f"Precio final: {total:.2f}")          

