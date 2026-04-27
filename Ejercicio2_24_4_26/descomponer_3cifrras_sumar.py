numero= int(input("Ingrese  numero de 3 ciras: "))
n3=numero % 10
n2 = (numero // 10) %10
n1 = (numero // 100)%10
suma = n1 + n2 +n3
print("La suma de los tres digitos es: "  ,suma)
numero= int(input("Ingrese  numero de 4 ciras: "))
n4 = numero % 10
n3= (numero//10)%10
n2 = (numero //100)%10
n1= (numero//1000)%10
#multiplicar entre si las cuatro cifras
multiplicacion = n1*n2*n3*n4
print("La multiplicacion de los cuatro digitos es: ", multiplicacion)
