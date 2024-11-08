from math import sqrt, exp


class Punto():

    def __init__(self, x, y):
        self.x = x
        self.y = y
                 

    def __str__(self):
        cadena = f"el punto esta ubicado en la coordenada: X= {self.x} Y= {self.y}"
        return cadena

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("se situa sobre el cuadrante 1")
        elif self.x < 0 and self.y > 0:
            print("se situa sobre el cuadrante 2")
        elif self.x < 0 and self.y < 0:
            print("se situa sobre el cuadrante 3")
        elif self.x > 0 and self.y < 0:
            print("se situa sobre el cuadrante 4")
        elif self.x == 0 and self.y != 0:
            print("se situa sobre el eje Y")
        elif self.x != 0 and self.y == 0:
            print("se situa sobre el eje X")
        else:
            print("Origen")

    def vector(self,x2,y2):
        try:
            x2 = int(input("Ingrese coordenada X: "))
        except ValueError:x2 = 0
        try:
            y2 = int(input("Ingrese coordenada Y: "))
        except ValueError:y2 = 0
        print(f"vector( {x2-self.x}, {y2-self.y})")

        
    def distancia(self,x2,y2):
        d= sqrt(exp(x2-self.x)+exp(y2-self.y))
        print("la distancia es",d,"punto")
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

 

print(A,B)
A.cuadrante()
B.cuadrante()
# punto.vector()
# punto.distancia()    