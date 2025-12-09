import random
import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6]) # Unidimensional

# arr = np.array([[1, 2, 3], [4, 5, 6]]) # Bidimencional



# Listas

L = ["L","i","s","t","a","f","w"]
    # 0 , 1 , 2 , 3 , 4 , 5 , 6  
# print(L)

# print(len(L))

# for i in range(0,len(L)): 
#     print(L[i])

# print("")    

# for i in L:
#     print(i)


############################################################################################################# 

# Matrices

# 1: 2x2

matrix = [[1, 2], 
          [3, 4]]

# print(matrix[0][1]) # Coordenadas (X,Y)

# for Fila in matrix:
#     for Elemento in Fila:
#         print(Elemento)

# for Fila in matrix:
#     for Elemento in Fila:
#         print(Elemento, end=' ') #Este parámetro en la función print evita el salto de línea que ocurre por defecto después de cada elemento, y en su lugar agrega lo que se defina entre las comillas simples.
#     print()  # Para hacer un salto de línea después de cada fila


############################################################################################################# 

# # Ingresar número de columnas y filas
# y = int(input("Digite el número de filas de la matriz: "))
# x = int(input("Digite el número de columnas de la matriz: "))

# # Crear una matriz vacía
# matriz = []

# # Construir la matriz
# for i in range(y):
#     fila = []
#     print(f"Ingresando los valores para la fila {i+1}:")
#     for j in range(x):
#         valor = int(input(f"Digite el valor para el elemento (Fila:{i}, Columna:{j}): "))
#         #valor = random.randint(0, 100)  # Generar valor aleatorio entre 0 y 100
#         fila.append(valor) 
#     matriz.append(fila)

# # Mostrar la matriz 
# print("\nLa matriz ingresada es:")
# for fila in matriz:
#     for elemento in fila:
#         print(f"|{elemento}|", end=' ')
#     print()    

# for fila in matriz:
#     print(fila)