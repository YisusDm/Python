from os import name, system

Swich = True

def limpiar():
    #Limpia la linea de comandos
    if name == "nt":
        system("cls")
    else:
        system("clear")

def ObtenerFecha(horas):
    if horas >= 0 and horas <= 30: #Hasta 30 Horas
        fecha = "15 de enero"
    elif horas > 30 and horas < 60: # Mas de 30 y menos de 60
        fecha = "15 de febrero"
    elif horas >= 60 and horas <= 90: # Entre 60 y 90
        fecha = "15 de marzo"    
    else: # mas de 90
        fecha = "15 de abril"    
    return fecha    

def continuar():
    while True:
        opcion = input("¿Desea continuar? (si/no): ")
        if opcion.lower() == "si" or opcion.lower() == "no":
            break
        else:
            print("Error: Opción no válida. Ingrese'si' o 'no'.")
            
    if opcion.lower() == "si":
        limpiar()
        swich = True
    elif opcion.lower() == "no":
        limpiar()
        print("Gracias por utilizar el programa.")
        swich = False
    return swich    


while Swich == True:
    Horas = int(input("Ingrese numero de horas de practica: "))

    if Horas >= 0 and Horas <= 120:
        Fecha = ObtenerFecha(Horas)
        print(f"La fecha es: {Fecha}")
        Swich = continuar()
    else:
        print("Error: Horas no válidas. Ingrese un número entre 0 y 120.")



 