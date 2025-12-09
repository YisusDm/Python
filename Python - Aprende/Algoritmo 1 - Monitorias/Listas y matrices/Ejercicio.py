# programa que solicita al usuario la cantidad de matrices que desea sumar, 
# a su vez debe validar que el usuario este intentando sumar dos o mas matrices. 
# debera solicitar la cantidad de filas y columnas que tendran las matrices a sumar. 
# Debera solicitar los elementos que contendra cada matriz generada, 
# atraves de un mensaje en pantalla indicando la matriz actual, 
# asi como la fila y la columna dondes e introducira dicho elemento. 
# El programa debera realizar la suma de las matrices generadas por el usuario, 
# y,a traves de una impresion en pantalla, 
# mostrar todas las matrices incluyendo la matriz resultante en formato de matriz mostrando 
# las matrices horizontalmente e incluyendo los signos de suma e igual


# Nota: Para poder sumar o restar matrices, 
#     éstas deben tener el mismo número de filas y de columnas. 
#     Es decir, si una matriz es de orden 3×2 y otra de 3×3, 
#     no se pueden sumar ni restar. Esto es así ya que, 
#     tanto para la suma como para la resta, 
#     se suman o se restan los términos que ocupan el mismo lugar en las matrices.


import random

Matrices=[]

def AsignaMatriz():
    while True: # Solicitar la cantidad de matrices que desea sumar
        nMatriz = int(input("Digite la cantidad de matrices que desea sumar: "))
        if nMatriz<2:
            print("Debe ingresar al menos dos matrices para sumar.")
        else: 
            break 
    ContruirMatriz(nMatriz)


def FilasColumnas():
    while True: # Ingresar número de filas y columnas
        y = int(input("Digite el número de filas de la matriz: "))
        x = int(input("Digite el número de columnas de la matriz: "))
        if(x<1 and y<1):
            print("El número de filas")
        else: 
            break
    return (x,y)
    

def ContruirMatriz(nMatriz): # Construir la matriz
    x,y = FilasColumnas() # Obtener número de filas y columnas para la matriz actual
    for i in range(nMatriz):
        Matriz = []
        for j in range(x):
            Fila = []
            for k in range(y):
                #valor = int(input(f"Digite el valor para el elemento (Matriz:{i+1}, Fila:{j+1}, Columna:{k+1}): "))
                valor = random.randint(0, 9)  # Generar valor aleatorio entre 0 y 100
                Fila.append(valor)
            Matriz.append(Fila)
        Matrices.append(Matriz)
    MostrarMatrizInicial()
    SumarMatrices()           


def MostrarMatrizInicial(): # Mostrar la matriz 
    c=0       
    print("\nLa matriz ingresada es:")
    for matriz in Matrices:
        c+=1
        print(f"Matriz: {c}")
        for fila in matriz:
            for elemento in fila:
                print(f"|{elemento}|", end=' ')
            print() 

def SumarMatrices(): # Sumar las matrices
    Suma = []
    for i in range(len(Matrices[0])):
        Fila = []
        for j in range(len(Matrices[0][0])):
            SumaElemento = 0
            for k in range(len(Matrices)):
                SumaElemento += Matrices[k][i][j]
            Fila.append(SumaElemento)
        Suma.append(Fila)
    print("\nLa matriz resultante es:")
    MostrarMatriz(Suma)

def MostrarMatriz(MatrizR): # Mostrar la matriz Resultante 
    for fila in MatrizR:
        for elemento in fila:
            print(f"|{elemento}|", end=' ')
        print()


AsignaMatriz()