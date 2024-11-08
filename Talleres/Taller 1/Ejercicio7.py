x=int
print("Ingrese numero:")
x= input()


Ing = int(input("Digite la cantidad total de ingresos anuales: "))
print("seleccione su estado civil:")
print("1-Soltero ")
print("2-Casado")
E_Civil = int(input("Digite aqui: "))
print("¿Tiene hijos?")
print("1-SI")
print("2-NO")
H = int(input("Digite aqui: "))

if(Ing == 20000000):
    print("Prestamo concedido")
else:
    if(Ing < 20000000 and Ing > 12000000 and E_Civil == 1):
        #if(E_civil == 1):
        print("Prestamo concedido") 
    else:
        if(Ing < 20000000 and Ing > 15000000 and E_Civil == 2 and H == 2):   
            print("Prestamo concedido")
        else:
            print("NO se le concede el prestamo por que no cumple")
            print("con los requisitos.")        