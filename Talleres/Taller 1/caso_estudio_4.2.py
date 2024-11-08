from datetime import datetime, timedelta

horaInicio =  int(input("Ingresa la hora: "))
while horaInicio<0 or horaInicio>23:
	horaInicio = int(input("Hora invalida, debe ser entre las 0 y 23 horas: "))

minutoInicio = int(input("Ingrese el minuto: "))
while minutoInicio<0 or minutoInicio>59:
	minutoInicio = int(input("Minuto invalido, debe ser entre los 0 y 59 minutos: "))

duracion = int(input("Ingrese cuantos minutos durara el evento: "))

hora1=f"{horaInicio}:{minutoInicio}"
hora1=datetime.strptime(hora1,"%H:%M")
horaFinalizacion=hora1 + timedelta(minutes=duracion)
print(horaFinalizacion.strftime('%H:%M'))

