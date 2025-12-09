while True:
    while True:
        edad = int(input("Digite su edad:"))
        if edad > 0:
            break
        else:
            print("Ingrese un valor de edad valido")

    if edad > 0 and edad <= 12:
        print("Usted es un niño")
    elif edad >= 13 and edad <= 17:
        print("Usted es un adolescente")
    elif edad >= 18 and edad <= 64:
        print("Usted es un adulto")
    else:
        print("Usted es un adulto mayor")                    