
swich = True #Variable que controla la condicion de entrada
LsTriagulo =["Equilatero","Isoseles","Escaleno"] #Posibles entradas validas

def mayus(texto): #funcion para convertir texto a Mayusculas
    return texto.upper()

def minus(texto): #funcion para convertir texto a Minusculas
    return texto.lower()

while swich == True:
    print("Tipos de Triangulo: \n Equilatero\n Isoseles \n escaleno ")
    Triangulo = input("Ingre el tipo de triangulo: ")
    if minus(Triangulo) in [minus(t) for t in LsTriagulo]: # Validar si el tipo de triángulo ingresado coincide con los valores en la lista
        swich = False
    else:
        print("Tipo de triángulo no válido, intente nuevamente.")

if minus(Triangulo) == minus(LsTriagulo[0]) and mayus(Triangulo) == mayus(LsTriagulo[0]):
    print(f"El triangulo {mayus(Triangulo)}: Todos los lados son iguales")
elif minus(Triangulo) == minus(LsTriagulo[1]) and mayus(Triangulo) == mayus(LsTriagulo[1]):
    print(f"El triangulo {mayus(Triangulo)}: Dos de sus lados son iguales")
elif minus(Triangulo) == minus(LsTriagulo[2]) and mayus(Triangulo) == mayus(LsTriagulo[2]):
    print(f"El triangulo {mayus(Triangulo)}: Todos sus lados son diferentes")    

