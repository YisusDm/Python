from time import strftime, localtime, sleep
from datetime import datetime
from json import dump, loads
from funcionesBuscaminas import *
def leerJSON(JSON):
    with open(JSON, "r", encoding="utf8") as f_obj:
            json = f_obj.read()
            f_obj.close()
    return json

def guardarSCORE(score):
    jsonscores = leerJSON("scores.json")
    scores = loads(jsonscores)
    score['fecha'] = datetime.now().timestamp()
    scores["scores"].append(score)
    with open("scores.json", 'w', encoding="utf8") as file:
            dump(scores, file, indent=4)#Almacena los scores en formato JSON
            file.close()

def verTopsJugadores():
    jsonscores = leerJSON("scores.json")
    scores = loads(jsonscores)['scores']
    tops = sorted(scores, key=lambda score : score['puntos'])
    top = -1
    limpiar()
    tablaPuntaje = [["TOP 5 JUGADORES"], ["Fecha", "Jugdador", "SCORES", "Tipo de juego"]]
    puntajeJugador = []
    for i in range(5):
        try:
            fechaPartida = strftime('%Y/%m/%d-%H:%M:%S', localtime(tops[top]['fecha']))
            puntajeJugador.append(fechaPartida)
            puntajeJugador.append(tops[top]['name'])
            puntajeJugador.append(tops[top]['puntos'])
            puntajeJugador.append(tops[top]['dificultad'])
            tablaPuntaje.insert(i+2,puntajeJugador)
            puntajeJugador = []
        except:
            pass
        top -= 1
    print(tabulate(tablaPuntaje))
    input("Presione ENTER para volver al menu principal")

def preguntas(score, minas_sin_marcar):
    from listPreguntas import preguntas
    cantidadPreguntas = len(preguntas)
    indicePregunta = randint(0,cantidadPreguntas-1)
    pregunta = preguntas[indicePregunta]['pregunta']
    while True:
        limpiar()
        print("¡HA EXPLOTADO UNA MINA!")
        ii = 1
        indicesRespuestaSalidas = []
        ordenAleatorioRespuestas = {}
        print(pregunta)
        while ii <= 4:
            indiceRespuesta = randint(0,3)#Genera el numero para el orden aleaorios de las respuestas
            respuesta = preguntas[indicePregunta]['respuestas'][indiceRespuesta]
            if indiceRespuesta not in indicesRespuestaSalidas:#Verifica que la resouesta ya no ha salido
                print("{}. {}".format(ii, respuesta))
                ordenAleatorioRespuestas[str(ii)] = respuesta
                indicesRespuestaSalidas.append(indiceRespuesta)
                ii += 1
        respuestaUsuario = input("Ingrese el numero de la respuesta correcta: ")
        respuestaCorrecta = preguntas[indicePregunta]['respuestas'][0]
        if respuestaUsuario != '' and (0 < int(respuestaUsuario) <= 4):
            if ordenAleatorioRespuestas[respuestaUsuario] == respuestaCorrecta:
                limpiar()
                print("Respuesta correcta")
                input("Presione ENTER para continuar jugando.")
                score['puntos'] += 1
                minas_sin_marcar -= 1
                jugando = True
                break
            else:
                limpiar()
                print("Respuesta incorrecta")
                jugando = False
                break
        else:
            limpiar()
            print("No ha ingresado una respuesta o el valor no esta entre 1-4")
            input("Presione ENTER para continuar jugando.")
    return jugando