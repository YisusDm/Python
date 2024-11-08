Mientras=True
print("¡Hola! Bienvenido al museo de Python")
print("Si deseas saber el precio de tu entrada, ", end="")
while(Mientras==True):
    edad = int(input("por favor indica tu edad: "))
    if(edad<=0):
        print("indique una edad valida")
    else:
        Mientras=False    

if(edad<=6):
    print("**Su entrada es totalmente gratis**")
    print("El precio de la entrada sin descuento es de 0 Euros.")
    print("Con el descuento son: 0 Euros")
else:    
    if(edad>6 and edad<=21):
        Precio=9
    elif(edad>21 and edad<67):
        Precio=14
    elif(edad>67):
        Precio=6
    
    print("¡De acuerdo!, ", end="")
    R_Bono = input("Tienes bono de descuento del 10%, para este mes? (s/n): ")
    if(R_Bono=="s" or R_Bono=="S"):
        Precio_Descuento = Precio*0.9
        print(f"El precio de la entrada sin descuento es de {Precio} Euros.")
        print(f"Con el descuento son: {Precio_Descuento} Euros")
    else:
        print(f"El precio de la entrada sin descuento es de {Precio} Euros.") 
