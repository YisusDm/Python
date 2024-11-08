from os import system, name
from random import randint
from tabulate import tabulate
import time

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

def coloca_pistas(tablero, fil, col):
    for y in range(1,fil+1):
        for x in range(1,col+1):
            if tablero[y][x] == "Ω":
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if 0 <= y+i <= fil and 0 <= x+j <= col:
                            if tablero[y+i][x+j] != "Ω":
                                tablero[y+i][x+j] += 1

    return tablero


def tipoJuego():
    while True:
        limpiar()
        opcion = input("[1. Iniciar Partida Aleatoria]\n[2. Crear Partida Manual]\nEscoge una opcion: ")
        limpiar()
        if opcion == "1":
            while True:
                limpiar()
                dificultad = input("[1. Facil]\n[2. Medio]\n[3. Dificil]\nEscoge el nivel de dificultad: ")
                if dificultad == "1":
                    filas = 15
                    columnas = 15
                    minas = 30
                    dificultad = "Aleatoria: Facil"
                    break
                elif dificultad == "2":
                    filas = 25
                    columnas = 25
                    minas = 50
                    dificultad = "Aleatoria: Medio"
                    break
                elif dificultad == "3":
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
    fil += 1
    col += 1
    while len(ceros) > 0:
        y, x = ceros.pop()
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 1 <= y+i <= fil-1 and 1 <= x+j <= col-1:
                    if visible[y+i][x+j] == val and oculto[y+i][x+j] == 0:
                        visible[y+i][x+j] = 0
                        if (y+i, x+j) not in ceros:
                            ceros.append((y+i, x+j))

                    else:
                        if oculto[y+i][x+j] != "Ω":
                            visible[y+i][x+j] = oculto[y+i][x+j]

    return visible

def tablero_completo(tablero, fil, col, val):
    for y in range(fil):
        for x in range(col):
            if tablero[y][x] == val:
                return False
    return True

def solicitarCoordenadas(filas, columnas, visible, score, minas_sin_marcar):
    while True:
        limpiar()
        print("SCORE {}".format(score['puntos']))
        print("MINAS:", minas_sin_marcar)
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

def portada():
    limpiar()
    print("╔═════════════════════════════════════════╗")
    print("║                                         ║")
    print("║            »BUSCAMINAS Python«          ║")
    print("║              »BOOTCAMP 2021«            ║")
    print("║                                         ║")
    print("║   Desarrollado por:                     ║")
    print("║           *Carlos iriarte               ║")
    print("║            *Isaias Palacio              ║")
    print("║             *Jesus Marquez              ║")
    print("║                                         ║")
    print("║                  ADSI57                 ║")
    print("║                   SENA                  ║")
    print("║                 ATLANTICO               ║")
    print("╚═════════════════════════════════════════╝")
    time.sleep(5)
    # limpiar()

def reglasJuego():
    limpiar()
    print("""Instrucciones del juego Buscaminas
            
    El juego consiste en despejar todas las casillas de una pantalla que no oculten una mina.
    Algunas casillas tienen un número, el cual indica la cantidad de minas que hay en las casillas circundantes. 
    Así, si una casilla tiene el número 3, significa que de las ocho casillas que hay alrededor hay 3 con minas y 5 sin minas. 
    Si se descubre una casilla sin número indica que ninguna de las casillas vecinas tiene mina y éstas se descubren automáticamente.
    Si se descubre una casilla con una mina se pierde la partida.
    
    Se puede poner una marca en las casillas que el jugador piensa que hay minas para ayudar a descubrir las que están cerca.
           """)   
    print("""Niveles de Juego
    El juego también posee un sistema de récords para cada uno de los 4 niveles en el que se indica el menor score obtenido al final de la partida. 
    Los niveles son:
            Nivel principiante: 15 × 15 casillas y 30 minas.
            Nivel intermedio: 25 × 25 casillas y 50 minas.
            Nivel experto: 35 × 35 casillas y 70 minas.
            Nivel personalizado: en este caso el usuario personaliza su juego eligiendo el número de minas y el tamaño de la cuadrícula.""")

    print("""Para el desplazamiento en el tablero nos basamos en coordenadas (eje X) y (eje Y) horizontal y vertical 
    """) 
    input("Para volver a la pantalla de inicio presione enter:")     