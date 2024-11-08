from os import system, name
from random import randint
from tabulate import tabulate

def limpiar():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def crea_tablero(fil, col, val):
    cabezera = []
    for i in range(col+1):
        cabezera.append(i)
    tablero=[]
    for i in range(fil):
        tablero.append([i+1])
        for j in range(col):
            tablero[i].append(val)
    tablero.insert(0, cabezera)
    return tablero

def coloca_minas(tablero, minas, fil, col):
    minas_ocultas = []
    numero = 0
    while numero < minas:
        y = randint(1, fil)
        x = randint(1, col)
        if tablero[y][x] != "Ω":
            tablero[y][x] = "Ω"
            numero +=1
            minas_ocultas.append((y,x))
    return tablero,minas_ocultas

tablero = crea_tablero(15, 15, 0)
tablero1 = tabulate(tablero)
print(tablero1)
print("##################################")
tablero, minas_ocultas = coloca_minas(tablero, 15, 15, 15)
tablero2 = tabulate(tablero)
print(tablero2)
print(minas_ocultas)

def coloca_pistas(tablero, fil, col):
    for y in range(fil):
        for x in range(col):
            if tablero[y][x] == "Ω":
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if 0 <= y+i <= fil-1 and 0 <= x+j <= col-1:
                            if tablero[y+i][x+j] != "Ω":
                                tablero[y+i][x+j] += 1

    return tablero 

def tipoJuego():
    while True:
        limpiar()
        opcion = input("[1. Iniciar Partida Aleatoria]\n[2. Crear Partida Manual]\nEscoge una opcion: ")
        if opcion == "1":
            while True:
                limpiar()
                dificultad = input("[1. Facil]\n[2. Medio]\n[3. Dificil]\nEscoge el nivel de dificultad: ")
                if opcion == "1":
                    filas = 15
                    columnas = 15
                    minas = 30
                    dificultad = "Aleatoria: Facil"
                    break
                elif opcion == "2":
                    filas = 25
                    columnas = 25
                    minas = 50
                    dificultad = "Aleatoria: Medio"
                    break
                elif opcion == "3":
                    filas = 35
                    columnas = 35
                    minas = 70
                    dificultad = "Aleatoria: Dicifil"
                    break
                else:
                    print("¡Escoja una de las dos opciones del menu!")
                    input("Presione ENTER")
            break
        elif opcion == "2":
            print("Crear Partida Manualmente")
            dificultad = "Partida Creada"
            while True:
                try:
                    filas = int(input("Numero de Filas: "))
                    columnas = int(input("Numero de Columnas: "))
                    break
                except:
                    print("En filas y columnas debe ingresar un numero")
            while True:
                minas = int(input("Numero de Minas: "))
                if minas < filas * columnas:
                    break
                print ("El numero de minas deber ser menor de %d."%(filas*columnas))
            dificultad = "Partida Creada" + str(columnas) + "*" + str(filas) + " Minas-" + str(minas)
            break
        else:
            print("¡Escoja una de las dos opciones del menu!")
            input("Presione ENTER")
    visible = crea_tablero(filas, columnas, "■")
    oculto = crea_tablero(filas, columnas, 0)
    oculto, minas_ocultas = coloca_minas(oculto, minas, filas, columnas)
    oculto=coloca_pistas(oculto, filas, columnas)
    return filas, columnas, visible, oculto, minas_ocultas, dificultad

def muestra_tablero(tablero):
    tablero = tabulate(tablero)
    print(tablero)

def rellenado(oculto, visible, y, x, fil, col, val):
    ceros = [(y,x)]
    while len(ceros) > 0:
        y, x = ceros.pop()
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 0 <= y+i <= fil-1 and 0 <= x+j <= col-1:
                    if visible[y+i][x+j] == val and oculto[y+i][x+j] ==0:
                        visible[y+i][x+j] = 0
                        if (y+i, x+j) not in ceros:
                            ceros.append((y+i, x+j))

                    else:
                        visible[y+i][x+j] = oculto[y+i][x+j]

    return visible  

def tablero_completo(tablero, fil, col, val):
    for y in range(fil):
        for x in range(col):
            if tablero[y][x] == val:
                return False
    return True

def solicitarCoordenadas(filas, columnas, visible, score):
    while True:
        limpiar()
        print("SCORE {}".format(score['puntos']))
        muestra_tablero(visible)
        try:
            x = int(input("Ingrese la coordenada X(horizontal): "))
            y = int(input("Ingrese la coordenada Y(vertical): "))
            if 1 <= x <= filas:
                if 1 <= y <= columnas:
                    break
                else:
                    print("El coordenada Y debe ser entre 1 y", filas)
                    input("Presione ENTER")
            else:
                print("El coordenada X debe ser entre 1 y", columnas)
                input("Presione ENTER")
        except:
            print("X debe ser un numero entre 1 y", columnas, " y Y debe ser un numero entre 1 y", filas)
            input("Presione ENTER")
    return y,x