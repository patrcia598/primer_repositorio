usuario= input("usuario (piedra,papel o tijera): ").lower()
computadora= input("computadora (piedra,papel o tijera): ").lower()
#creamos validacion inicial
opciones_validas = ["piedra","papel","tijera"]
if usuario not in opciones_validas or computadora not in opciones_validas:
    print("Error: uno de los jugadores ingreso una opcion invalida")
else:
    if usuario == computadora:
      print("empate")
    elif (usuario=="piedra" and computadora=="tijera") or \
         (usuario=="papel" and computadora=="piedra") or \
         (usuario=="tijera" and computadora=="papel"):

        print(" gana usuario!") 
    else:
        print("Gana computadora!")      