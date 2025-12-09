import numpy as np

filas = int(input("ingrese la cantidad de filas: "))
columnas = int(input("ingrese la cantidad de columnas: "))


pares = 0
impares = 0
ceros = 0
sumapares = 0
sumaimpares = 0

elementos = np.zeros((filas, columnas)) #Matriz Elementos

for fil in range(filas):
  for col in range(columnas):
    elementos[fil][col ] = int(input(f"ingrese el elemento fila {fil+1} columna {col+1}: ")) #Se remplaza valor del elemento
    if elementos[fil][col]== 0:
      ceros += 1
    elif elementos [fil][col] % 2 == 0:
      pares+= 1
      sumapares+= elementos[fil][col]
    else:
      impares+=1
      sumaimpares+= elementos[fil][col] 

# for i in elementos:
#   print(i)

if pares > 0:
  promediopares = sumapares / pares
else:
    promediopares = 0
if impares > 0:
  promedioimpares = sumaimpares / impares
else:
  promedioimpares = 0

print(f"cantidad de pares : {pares}")
print(f"promedio de pares : {promediopares}")
print(f"cantidad de impares : {impares}")
print(f"promedio de impares : {promedioimpares}")
print(f"cantidad de ceros: {ceros}")

