from tabulate import tabulate
import time
import random
import os

def limpiar(): 
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

def crea_tablero(fil, col, val):
    tablero=[]
    for i in range(fil):
        tablero.append([])
        for j in range(col):
            tablero[i].append(val)
    return tablero

def muestra_tablero(tablero):
    for fila in tablero:
        for elem in fila:
            print(elem, end=" ")
        print()

def coloca_minas(tablero, minas, fil, col):
    minas_ocultas = []
    numero = 0
    while numero < minas:
        y = random.randint(0,fil-1)
        x = random.randint(0, col-1)
        if tablero[y][x] != 9:
            tablero[y][x] = 9
            numero +=1
            minas_ocultas.append((y,x))
    return tablero,minas_ocultas

def coloca_pistas(tablero, fil, col):
    for y in range(fil):
        for x in range(col):
            if tablero[y][x] == 9:
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if 0 <= y+i <= fil-1 and 0 <= x+j <= col-1:
                            if tablero[y+i][x+j] != 9:
                                tablero[y+i][x+j] += 1

    return tablero                        

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

def presentacion():
    print("╔════════════════════════════════╗")
    print("║                                ║")
    print("║          »BUSCAMINAS«          ║")
    print("║                                ║")
    print("║      [w/s/a/d] - Moverse       ║")
    print("║                                ║")
    print("║        [m] - Mostrar           ║")
    print("║                                ║")
    print("║        [b] - Marcar            ║")
    print("║        [v] - Desmarcar         ║")
    print("║                                ║")
    print("╚════════════════════════════════╝")
    time.sleep(5)
    limpiar()

def menu():
    print()
    print("╔════════════════════════════════╗")
    print("║      [w/s/a/d] - Moverse       ║")
    print("║        [m] - Mostrar           ║")
    print("║        [b] - Marcar            ║")
    print("║        [v] - Desmarcar         ║")
    print("╚════════════════════════════════╝")
    opcion = input("Accion: ")
    return opcion

columnas = 15
filas = 15
visible = crea_tablero(filas,columnas,"■")
oculto = crea_tablero(filas, columnas, 0)
oculto, minas_ocultas = coloca_minas(oculto, 15, filas, columnas)
oculto=coloca_pistas(oculto, filas, columnas)
presentacion()

y = random.randint(2, filas-3)
x = random.randint(2, columnas-3)

real = visible[y][x]
visible[y][x] = "x"
limpiar()

muestra_tablero(visible)

minas_marcadas = []

jugando = True

while jugando:
    mov = menu()

    if mov == "w" or mov == "W":
        if y==0:
            y=0
        else:
            visible[y][x] = real
            y -= 1
            real = visible[y][x]
            visible[y][x] = "x"
    elif mov == "s" or mov == "S":
        if y == filas-1:
            y = filas-1
        else:
            visible[y][x] = real
            y += 1
            real = visible[y][x]
            visible[y][x] = "x"
    elif mov == "a" or mov == "A":
        if x == 0:
            x=0
        else:
            visible[y][x] = real
            x -= 1
            real = visible[y][x]
            visible[y][x] = "x"
    elif mov == "d" or mov == "D":
        if x == columnas-1:
            x = columnas-1
        else:
            visible[y][x] = real
            x += 1
            real = visible[y][x]
            visible[y][x] = "x"
    elif mov ==  "b" or mov == "B":
        if real == "■":
            visible[y][x] = "Δ"
            real = visible[y][x]
            if (y,x) not in minas_marcadas:
                minas_marcadas.append((y,x))
    elif mov == "v" or mov == "V":
        if real == "Δ":
            visible[y][x] = "■"
            real = visible[y][x]
            if (y,x) in minas_marcadas:
                minas_marcadas.remove((y,x))
    elif mov == "m" or mov == "M":
        if oculto[y][x] == 9:
            visible[y][x] ="Ω"
            jugando = False

        elif oculto[y][x] != 0:
            visible[y][x] = oculto[y][x]
            real = visible[y][x]

        elif oculto[y][x] == 0:
            visible[y][x] = 0
            visible = rellenado(oculto, visible, y, x, filas, columnas, "■")
            #visible = reemplaza_ceros(visible)
            real = visible[y][x]                                      
    
    limpiar()
    muestra_tablero(visible)
    ganas = False

    if tablero_completo(visible, filas, columnas, "■") and\
        sorted(minas_ocultas) == sorted(minas_marcadas) and\
            real != "■":
            ganas = True
            jugando = False


if not ganas:
    print("╔════════════════════════════════╗")
    print("║                                ║")
    print("║*********** GAME OVER **********║")
    print("║                                ║")
    print("╚════════════════════════════════╝")
else:
    print("╔════════════════════════════════╗")
    print("║                                ║")
    print("║************ YOU WIN ***********║")
    print("║                                ║")
    print("╚════════════════════════════════╝")  
