
Diccionarios = []

while True:
    Nombre =  input("Ingrese su nombre: ")
    Edad = int(input("Ingrese su edad: "))
    NPaises = int(input("Digite el numero de paises que ha visitado: "))
    Paises = []
    for i in range(NPaises):
        pais = input(f"Ingrese el nombre del pais {i+1}: ")
        Paises.append(pais)

    Diccionario = {'Nombre': Nombre, 
                   'Edad': Edad, 
                   'Paises': Paises}
    
    Diccionarios.append(Diccionario) 
    
    F = int(input("¿Desea continuar?  0 = Si o 1 = No : "))
    if F == 1:
        break

print(Diccionarios)

    
