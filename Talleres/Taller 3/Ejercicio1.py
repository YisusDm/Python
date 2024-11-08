numero_C=0
tipo_S=0
PS=True
SCA=0
contAltoconsumo=0

#validar
numero_S = int(input("Digite el numero de supcrictores: "))
for i in range (1,numero_S+1):
    numero_C = int(input("Digite numero de contrato: "))
    while(numero_C < 1000 or numero_C > 99999):
        #aggregar mas digitos como 00000
        print("El numero de contrato debe tener 5 digitos")
        numero_C = int(input("Digite numero de contrato: "))
    tipo_S = int(input("Tipo de supcrictor.\n 1.Residencial.\n 2.Comercial.\n... "))

    while(tipo_S!=1 and tipo_S!=2):
        print("Error, opción 1 o 2.")
        tipo_S = int(input("Tipo de supcrictor.\n 1.Residencial.\n 2.Comercial.\n... "))
        lectura_I = int(input("Digitar lectura inicial: "))
        lectura_F = int(input("Digitar lectura final: "))

    while  lectura_I > lectura_F or lectura_I == lectura_F or lectura_F == 0 :
        print("○--]====> Para no detectar error <====[--○ \n○ La lectura inicial debe ser menor a la lectura final \n○ las lesturas no pueden tener valores iguales.\n")
        lectura_I = int(input("Digitar lectura inicial: "))
        lectura_F = int(input("Digitar lectura final: "))
    lectura_T = lectura_F - lectura_I
    acum += lectura_T

    if lectura_T > 500 and tipo_S == 1 :
        contAltoconsumo += 1
        promedio_E = acum / contAltoconsumo
        if PS == True:
            primer_C = numero_C
            SCA = i
            PS = False
    print(f"El consumo del supcrictor {numero_S} es: {lectura_T}kwh\n")
if contAltoconsumo == 0 :
    print("No hubo promedio de supcrictores de alto consumo.")
else:
    print(f"Promedio de consumo eléctrico de los suscriptores de tipo residencial y de alto consumo es {:.2f}kwh ")
    print(f"El supcrictor residenncial {SCA} del contrato {numero_C} supera los 500kwh.")
print(f" Consumo eléctrico total de la zona: {acum} kwh")

