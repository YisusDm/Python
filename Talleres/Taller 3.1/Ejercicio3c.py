Swich=True
while(Swich==True):
  palabraIng = input("Ingrese la palabra (debe comenzar y terminar con la misma letra): ")
  #palabraIng = "abeja"
  palabra = palabraIng.upper()
  longitud=len(palabra)
  num=longitud
  longitud2=longitud-1
  letraInicial = palabra[0]
  letraFinal = palabra[-1]
  if (letraInicial == letraFinal):
    Swich=False
    print("Correcto")
    letras1 = []
    for i in range(longitud):
        letra1=palabra[i]
        nuevaLetra1 = letra1
        letras1.append(nuevaLetra1)
    letras2 = []
    for y in range(longitud2):
        letra2=palabra[y]
        nuevaLetra2 = letra2
        letras2.append(nuevaLetra2)    
    letras2[0]=""
    letras3 = []
    for x in range(longitud):
        letra3=palabra[x]
        nuevaLetra3 = letra3
        letras3.append(nuevaLetra3)    
    letras3[0]=""
  else:
    print("Incorrecto")

#imprimir
for i in range(0,longitud):
    y=i
    print (('  ' * (num - i - 1) +(letras1[i])),sep="",end="")
    if (i==longitud2):
      y=False
      for x in range(1,longitud):
        print (('   ' +(letras3[x])),end="") 
    print(('  ' * (2*y) +(letras2[y])))