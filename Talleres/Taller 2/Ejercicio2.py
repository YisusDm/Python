while(True):
    print("Digite las dimenciones del triagulo.")
    A = int(input("Lado 1: "))
    B = int(input("Lado 2: "))
    C = int(input("Lado 3: "))

    if(A>B and A>C):
        Hip=(A)**2
        H=(B**2)+(C**2)
    elif(B>A and B>C):
        Hip=(B)**2
        H=(A**2)+(C**2)
    else: 
        Hip=(C)**2
        H=(A**2)+(B**2)      
    
    if(Hip == H):
        print("El triangulo es rectangulo")
    elif(A==B and A==C and B==C): 
        print("El triangulo es equilátero")     
    elif(A==B or A==C or B==C):
        print("El Triangulo es isósceles") 
    else:
        print("El triangulo es escaleno")           