from Bus import Bus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

bus1= Bus(input('Digite la placa del bus: '),int(input('Digite la capacidad: ')),float(input('Digite el precio del pasaje: ')))
bus1.getPasajerosActuales()
bus1.getPrPasaje()
bus1.getCapacidad()
bus1.getPlaca()
bus1.subirPasajeros(int(input('Digite el numero de pasajeros que se va a subir: ')))
bus1.getPasajerosActuales()
bus1.bajarPasajeros(int(input('Digite el numero de pasajeros que se va a bajar: ')))
bus1.subirPasajeros(int(input('Digite el numero de pasajeros que se va a subir: ')))
bus1.getPasajerosActuales()
bus1.getPasajerosTotales()
bus1.getDineroAcumulado()