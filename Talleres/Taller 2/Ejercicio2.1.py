import math
#1
"""
HorasTrabajadas=int(input("Digite las horas trabajadas mensualmente "))
PrecioPorHora=float(input("Digite el valor por hora de trabajo"))
if (HorasTrabajadas>40):
    HorasExtras=HorasTrabajadas-40
    if(HorasExtras>8):
        HorasExtrasTriples=HorasExtras-8
        SueldoTotal=HorasExtrasTriples*(PrecioPorHora*3)+(8*(PrecioPorHora*2))
        SueldoTotal=SueldoTotal+(40*PrecioPorHora)
        print("sus salario total es:",SueldoTotal)
    else:
        SueldoTotal=HorasExtras*(PrecioPorHora*2)
        SueldoTotal=SueldoTotal+(40*PrecioPorHora)
        print("sus salario total es:",SueldoTotal)
else:
    SueldoTotal=HorasTrabajadas*PrecioPorHora
    print("sus salario total es:",SueldoTotal) 
"""
#2    

A=float(input("Digite El Valor de A"))
B=float(input("Digite El Valor de B"))
C=float(input("Digite El Valor de C"))

NumeroMayor=max(A, B, C)

if (A==B and B==C and C==A) :
    print(" el triangulo es equilatero ")
elif(A==B or B==C or C==A ):
    print(" el triangulo es isoceles ")
else:
   if(A>B or A>C):
      Hipotenusa=int(math.sqrt(pow(B,2) + pow(C,2)))
      
      if(Hipotenusa==A):
          print("El triangulo es rectangulo")
      else:    
         print("El triangulo es escaleno")  
   elif(A<B and A<C and C<=B):
       CatetoA=math.sqrt(pow(B,2) - pow(C,2))
       if(CatetoA==A):
            print("El triangulo es rectangulo")
       else:
           print("El triangulo es escaleno")  
   elif(A<B and A<C and C>=B) :
       CatetoA=math.sqrt(pow(C,2) - pow(B,2))
   else:
       print("El Triangulo es isoceles")
       