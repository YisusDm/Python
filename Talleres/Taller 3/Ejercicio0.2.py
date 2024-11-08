#N (Numero de trabajadores)


gasto_Total = 0

valor = float(input("Digite el valor a pagar por hora laborada:"))
N = int(input("Digite la cantidad de trabajadores:"))
for i in range (1, N+1):
    MientrasDias=True
    while(MientrasDias==True):
        Dias = int(input(f"{i}: Digite la cantidad de dias que trabajo en la semana en rango de (1-7) : "))
        if(Dias>7):
            print("Digite dias de la semana validos")
        else:    
            MientrasDias = False   
            
    pago_semana = 0
    for j in range (1, Dias+1):
        MientrasHoras=True
        while(MientrasHoras==True):
            Horas = int(input(f"Digite la cantidad de horas laboradas en el dia {j}: "))
            if(Horas>=24):
                print("Digite una hora valida")
            else:
                MientrasHoras = False
                Pago_Dia = Horas*valor
                pago_semana = pago_semana+Pago_Dia

    print(f"El total a pagar al trabajador {i} en la semana es: {pago_semana}")
    gasto_Total=gasto_Total+pago_semana

print(f"El costo asumido por la empresa en la semana por {N} trabajadores es de: {gasto_Total}")