a=int(input("Ingresar un numero : "))
b = int(input("Ingresar un numero : "))
c = int(input("Ingresar un numero : "))
if (a >= b and a>=c):
    if (b>=c):
        print (a,b,c)
    else:
        print(a,c,b)  
if (b>=a and b>=c):
    if(a>=c) :
        print(b,a,c)
    else:  
        print(b,c,a) 
if (c>= a and c>=b) :
    if (b>= a) :
        print(c,b,a) 
    else:
        print(c,a,b)               