from funcionesPreguntas import *
from instalarRequisitos import *
instalarRequisitos()
portada()
while True:
    limpiar()
    action = input("""1. Iniciar Nueva Partida\n2. Ver Tops 5\n3. Leer instrucciones de juego\n4. Salir del Progarama
    Elige la accion: """)
    if action == "1":
        score_jugador = {'puntos': 0}
        score_jugador['name'] = input("Ingrese su nombre: ")

        filas, columnas, visible, oculto, minas_ocultas, dificultad =tipoJuego()
        minas_sin_marcar = len(minas_ocultas)

        score_jugador['dificultad'] = dificultad    

        y, x = solicitarCoordenadas(filas, columnas, visible, score_jugador, minas_sin_marcar)
        #TEST
        # coordenadasSalidas = []
        # while True:
        #     y = randint(1,filas)
        #     x = randint(1,columnas)
        #     coordenada = (y,x)
        #     if coordenada not in coordenadasSalidas:
        #         coordenadasSalidas.append((y,x))
        #         break
        real = visible[y][x]
        visible[y][x] = "x"
        limpiar()
        minas_marcadas = []
        jugando = True
        while jugando:
            while True:
                limpiar()
                print("SCORE {}".format(score_jugador['puntos']))
                print("MINAS:", minas_sin_marcar)
                muestra_tablero(visible)
                accion = input("1. Mostrar\n2. Marcar\n3. Desmarcar\nIngrese la accion a hacer en la coordenada: ")
                if accion == "1":
                    if real == "■":
                        if oculto[y][x] == "Ω":
                            visible[y][x] = "Ω"
                            real = visible[y][x]
                            if (y,x) not in minas_marcadas:
                                minas_marcadas.append((y,x))
                                minas_sin_marcar -= 1
                            jugando = preguntas(score_jugador, minas_sin_marcar)
                            
                        elif oculto[y][x] != 0:
                            visible[y][x] = oculto[y][x]
                            real = visible[y][x]
                            score_jugador['puntos'] += 5

                        elif oculto[y][x] == 0:
                            visible[y][x] = 0
                            visible = rellenado(oculto, visible, y, x, filas, columnas, "■")
                            real = visible[y][x] 
                            score_jugador['puntos'] += 10
                        break
                    else:
                        print("Ya ha mostrado esta casilla")
                        input("Presione ENTER")
                        visible[y][x] = real
                        break        
                elif accion == "2":
                    if real == "■":
                        visible[y][x] = "Δ"
                        real = visible[y][x]
                        if (y,x) not in minas_marcadas:
                            minas_marcadas.append((y,x))
                            minas_sin_marcar -= 1
                    break
                elif accion == "3":
                    if real == "Δ":
                        visible[y][x] = "■"
                        real = visible[y][x]
                        if (y,x) in minas_marcadas:
                            minas_marcadas.remove((y,x))
                            minas_sin_marcar += 1
                    break
                else:
                    print("¡Escoja una de las tres opciones del menu!")
                    input("Presione ENTER")                             
            
            limpiar()
            print("SCORE {}".format(score_jugador['puntos']))
            muestra_tablero(visible)
            ganas = False

            if tablero_completo(visible, filas, columnas, "■") and\
                sorted(minas_ocultas) == sorted(minas_marcadas) and\
                    real != "■":
                    ganas = True
                    jugando = False
            if jugando == True:
                y, x = solicitarCoordenadas(filas, columnas, visible, score_jugador, minas_sin_marcar)
                #TEST
                # while True:
                #     y = randint(1,filas)
                #     x = randint(1,columnas)
                #     coordenada = (y,x)
                #     if coordenada not in coordenadasSalidas:
                #         coordenadasSalidas.append((y,x))
                #         break
                real = visible[y][x]
                visible[y][x] = real
                visible[y][x] = "x"
                limpiar()

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
        guardarSCORE(score_jugador)
        input("Presione ENTER para volver al menu principal")

    
    elif action == "2":
        verTopsJugadores()
    
    elif action == "3":
        reglasJuego()    
    
    elif action == "4":
        break
    else:
        print("¡Escoja una de las tres opciones del menu!")
        input("Presione ENTER") 
