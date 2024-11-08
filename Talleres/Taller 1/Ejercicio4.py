Hora=0
Minutos=0
Segundos=0

Mientras = True

while(Mientras):
  v=5
  HoraCadena = "12:57:34"
 # HoraCadena = input("Digite la hora de inicio del evento (HH:MM:SS) : ")
  HoraI =int(HoraCadena.split(":")[0])
  MinutosI =int(HoraCadena.split(":")[1])
  SegundosI =int(HoraCadena.split(":")[2])
  if(HoraI>23):
    print("Hora no valida digite una unidad correcta")
    v=v-1
  if(MinutosI>59):
    print("Minutos no validos digite una unidad correcta")
    v=v-1
  if(SegundosI>59):
    print("Segundos no validos digite una unidad correcta")
    v=v-1   
  if(v==5):
    print("La hora digitada es: ",HoraI,":",MinutosI,":",SegundosI)
    swich = int(input("Digite 1 para continuar o 2 para volver: "))
    if(swich==1):
      Mientras = False
    else:
        if(swich==0):
          Mientras = True

#print("Digite la cantidad de Horas minutos y segundos que dura el evento") 
#LimEvento =input("en (HH:MM:SS): ")
LimEvento =  "02:17:04"
HorasF =int(LimEvento.split(":")[0])
MinutosF =int(LimEvento.split(":")[1])
SegundosF =int(LimEvento.split(":")[2])

TimeS=SegundosI+SegundosF
TimeM=MinutosI+MinutosF
TimeH=HoraI+HorasF
if(TimeS>59):
  Segundos=TimeS-60
  TimeM=TimeM+1
else:
  Segundos=TimeS 
if(TimeM>59):
  Minutos=TimeM-60
  TimeH=TimeH+1
else:
  Minutos=TimeM 

  
print("El eveto termina a las: ",TimeH,":",Minutos,":",Segundos)   