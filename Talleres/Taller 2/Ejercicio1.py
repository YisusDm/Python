ValorHoraL = int(input("DIgite el valor a devengar por hora laborada: "))
HorasLaboradas = int(input("Digite la cantidad de horas laboradas: "))
if(HorasLaboradas > 40):
    HorasExtras = HorasLaboradas - 40
    TotalDevengadoBase = ValorHoraL * 40 
    if(HorasExtras > 8):
        HorasExtras1 = 8
        HorasExtras2 = HorasExtras - 8
        DevengadoE1 = (HorasExtras1 * ValorHoraL)*2
        DevengadoE2 = (HorasExtras2 * ValorHoraL)*3
        TotalDevengadoE = DevengadoE1+DevengadoE2
    else:
        TotalDevengadoE = (HorasExtras * ValorHoraL)*2
    
    TotalDevengado = TotalDevengadoBase + TotalDevengadoE
    print("Su cantidad de horas laboras fue de ",HorasLaboradas," y su salario neto es: ")
    print(TotalDevengado) 

elif(HorasLaboradas <= 40):
    TotalDevengado =  (HorasLaboradas*ValorHoraL) 
    print("Su cantidad de horas laboras fue de ",HorasLaboradas," y su salario neto es: ")
    print(TotalDevengado)     

