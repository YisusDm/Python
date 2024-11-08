MientrasH = True
MientrasM = True
while(MientrasH):
    hora = int(input("hora de inicio (horas): "))
    if(hora>23):
        print("Hora no valida por favor intente nuevamente")
    else:
        MientrasH = False    
while(MientrasM):
    min = int(input("Minutos de inicio (minutos): "))
    if(min>60):
        print("Minutos no valido por favor intente nuevamente")
    else:
        MientrasM = False    

dura = int(input("duracion del evento (minutos): "))
sumaMinutos=min+dura
totalMinutos=(sumaMinutos%60)
sumaHoras=int(sumaMinutos/60)+hora
totalHoras=sumaHoras%24
if(totalMinutos<10):
    print("el tiempo final es: ",totalHoras,":",0,"",totalMinutos, sep="")
else:    
    print("el tiempo final es: ",totalHoras,":",totalMinutos, sep="")
