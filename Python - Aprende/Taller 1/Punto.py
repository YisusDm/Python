from math import sqrt
class Punto():
    
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __str__(self):
        cadena =f"La coordenada: (X={self.x} Y={self.y})"
        print(cadena)

    def cuadrante(self):
        if self.x>0 and self.y>0:
            print("Se situa sobre el cuadrante 1")
        elif self.x<0 and self.y>0 :
            print("Se situa sobre el cuadrante 2")
        elif self.x<0 and self.y<0 :
            print("Se situa sobre el cuadrante 3")
        elif self.x>0 and self.y<0 :
            print("Se situa sobre el cuadrante 4") 
        elif self.x==0 and self.y!=0 :
            print("Se situa sobre el eje Y")
        elif self.x!=0 and self.y==0 :
            print("Se situa sobre el eje X")           
        else:
            print("Se situa en el punto de origen")          


    def vector(self,OtroPunto):
        if (OtroPunto.x-self.x<0):
            d1=abs(OtroPunto.x-self.x)
        else:d1=(OtroPunto.x-self.x)
        if (OtroPunto.y-self.y<0):       
            d2=abs(OtroPunto.y-self.y)
        else:d2=(OtroPunto.y-self.y)
        print(f"El vector resultante para los puntos {self.x,self.y} y {OtroPunto.x,OtroPunto.y}")    
        print(f"El vector es:( {d1}, {d2})")

    def distancia(self, OtroPunto):
        d= sqrt((OtroPunto.x-self.x)**2+(OtroPunto.y-self.y)**2)
        print(f"La distancia entre los puntos {self.x,self.y} y {OtroPunto.x,OtroPunto.y}")
        print("es de : ","{0:.2f}".format(d),"puntos")    

 
class Rectangulo:
    def __init__(self, Punto_Inicial=Punto(), Punto_Final=Punto()):
        self.Punto_Inicial = Punto_Inicial
        self.Punto_Final = Punto_Final
 
        self.Base = abs(self.Punto_Final.x - self.Punto_Inicial.x)
        self.Altura = abs(self.Punto_Final.y - self.Punto_Inicial.y)
        self.Area = self.Base * self.Altura
 
    def base(self):
        print(f"La base del rectángulo es: {self.Base}" )
 
    def altura(self):
        print(f"La altura del rectángulo es: {self.Altura}" )
 
    def area(self):
        print(f"El área del rectángulo es: {self.Area}" )

#Agregando valores a los objetos (A,B...)  
for i in range(2):
    try:
        x = int(input("Ingrese coordenada X: "))
    except ValueError:
        x = 0
        print("punto x=0")

    try:
        y = int(input("Ingrese coordenada Y: "))
    except ValueError:
        y = 0
        print("punto y=0")
    if i==0:
        A=Punto(x,y)
    else:
        B=Punto(x,y)

C = Punto(2,4)
D = Punto(-7,8)
E = Punto(-9,-2)
F = Punto(4,-5)
G = Punto(6,0)
H = Punto(0,6)
I = Punto(0,0)

#LLamado a mostrar los metodos:STR,CUADRANTE
A.__str__()
A.cuadrante()
B.__str__()
B.cuadrante()
C.__str__()
C.cuadrante()
D.__str__()
D.cuadrante()
E.__str__()
E.cuadrante()
F.__str__()
F.cuadrante()
G.__str__()
G.cuadrante()
H.__str__()
H.cuadrante()
I.__str__()
I.cuadrante()

#LLamado a mostrar metodo: VECTOR
A.vector(B)
B.vector(C)
C.vector(D)
D.vector(E)
E.vector(F)
F.vector(G)
G.vector(H)
H.vector(I) 
 
#LLamado a mostrar metodo: DISTANCIA
A.distancia(B)
B.distancia(C)
C.distancia(D)
D.distancia(E)
E.distancia(F)
F.distancia(G)
G.distancia(H)
H.distancia(I)
 
#LLamado a mostrar metodos del la clase rectangulo 
RTG = Rectangulo(A, B)
RTG.base()
RTG.altura()
RTG.area()         