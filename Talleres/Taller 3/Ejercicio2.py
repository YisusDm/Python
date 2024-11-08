#Parcial_Tiempo: Tiempo que tarda cada avion en recorrer 4600 km
Parcial_TiempoInicialG=4600 #4600 horas debido a que si es muy lento el avion es inposible volar a menos de 1km/h
Contador=0
Contador_ganador=0
Contador_Perdedor=0
Parcial_TiempoInicialP=0
Promedio_VelocidadF=0
Promedio_VelocidadNF=0
Promedio_VelocidadG=0
Promedio_VelocidadP=0
Distancia_Min=0
Distancia=0
X_tiempo=0
MientrasX=True

while(MientrasX==True):
    MientrasY=True
    Identificacion = input("Ingrese aqui la identificacion del vuelo: ")
    while(Distancia<=0):
        Distancia = float(input("Digite aqui la distancia recorrida (KM): "))
    while(X_tiempo<=0):    
        X_Tiempo = float(input("Digite aqui la duracion del vuelo (Horas): ")) 
    Contador += 1
    Velocidad =Distancia / X_Tiempo
    Parcial_Tiempo = (4600 / Velocidad)

    if(Distancia >= 4600):
        print(f"{Identificacion} Finalizo la carrera con exito, su velocidad fue de ", end=""   )
        print ("{0:.1f}".format(Velocidad),"Km/h")
        Promedio_VelocidadF += Velocidad 
        Contador_ganador += 1
        if(Parcial_Tiempo < Parcial_TiempoInicialG):
            Parcial_TiempoInicialG = Parcial_Tiempo
            Tiempo_Final_Ganador = Parcial_Tiempo
            Velocidad_Ganador =  Velocidad
            Avion_Ganador = Identificacion
    
    else:
        print(f"{Identificacion} No finalizo la carrera, su velociada promedio fue de ", end="")
        print ("{0:.1f}".format(Velocidad),"Km/h") 
        Promedio_VelocidadNF += Velocidad 
        Contador_Perdedor += 1
        if(Distancia > Distancia_Min):
            Distancia_Min = Distancia
            Distancia_perdedor = Distancia 
            Velocidad_Perdedor =  Velocidad
            Avion_Perdedor = Identificacion

    while(MientrasY==True):
        A_Competidor = input("Marque (S) para ingresar otro conpetidor o (N) para terminar: ")
        if(A_Competidor=="N" or A_Competidor=="n"):
            MientrasX=False
            MientrasY=False

        elif(A_Competidor=="S" or A_Competidor=="s"):
            MientrasY=False
        else:
            print("Seleccione una opcion valida")    

if(Contador_ganador>0):
    Porcentaje_Ganadores = (Contador_ganador*100/Contador)
    Promedio_Velocidad_Terminaron = Promedio_VelocidadF/Contador_ganador
    print("")
    print(f"El {Porcentaje_Ganadores}% de los corredores finalizaron la carrera con exito")
    print("")
    print("La velocidad promedio de los corredores que finalizaron la carrera fue de ", end="")
    print("{0:.1f}".format(Promedio_Velocidad_Terminaron),"km/h ")
    print("")
    print(f"EL ganador de la carrera de aviones fue {Avion_Ganador} con un promedio de velocidad de ", end="")
    print ("{0:.1f}".format(Velocidad_Ganador),"Km/h en una distancia de 4600km") 
else:
    Porcentaje_Ganadores=0
    Promedio_Velocidad_Terminaron=0 
    Avion_Ganador="Ninguno"
    Velocidad_Ganador=0   
if(Contador_Perdedor>0):
    Porcentaje_Perdedores = (Contador_Perdedor*100/Contador)
    Promedio_Velocidad_NTerminaron = Promedio_VelocidadNF/Contador_Perdedor
    print(f"El {Porcentaje_Perdedores}% de los corredores No finalizaron la carrera")
    print("")
    print("La velocidad promedio de los corredores que finalizaron la carrera fue de ", end="")
    print("{0:.1f}".format(Promedio_Velocidad_NTerminaron),"km/h ")
    print("")
    print(f"Entre los aviones que no pudieron terminar la carrera el que mas se aproximo a la meta fue {Avion_Perdedor} con un promedio de velocidad de ", end="")
    print ("{0:.1f}".format(Velocidad_Perdedor),f"Km/h en una distancia de {Distancia_perdedor}km") 

else:
    Porcentaje_Perdedores=0
    Promedio_Velocidad_NTerminaron=0
    Avion_Perdedor="Ninguno"
    Velocidad_Perdedor=0
    Distancia_perdedor=0


