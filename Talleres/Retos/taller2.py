import math
#este es el ejercicio del rectangulo, pero uní los dos ejercicios en uno para hacerlo más interesante.
class Punto:
    
    def __init__(self,nombre,x1=0,y1=0):
        self.nombre = nombre
        self.x1 = x1
        self.y1= y1
        

    def __str__(self):
        return (f"La cordenada es: ({self.x1},{self.y1})")
    #aqui creo una tupla la cual envio por medio de la funcion cordenada()
    def cordenada(self):
        return (self.x1,self.y1)
    
    def cuadrante(self):
        mensaje= (f"{self.nombre} se encuentra en el cuadrante: ")
        if self.x1==0 and self.y1 != 0:
            print(mensaje + ("y"))
        elif self.x1 != 0 and self.y1 == 0:
            print(mensaje + ("x"))
        elif self.x1 == 0 and self.y1 == 0:
            print(mensaje + ("Origen"))
        elif self.x1 >0 and self.y1 >0:
            print(mensaje + ("1"))
        elif self.x1 < 0 and self.y1 >0:
            print(mensaje + ("2"))
        elif self.x1 <0 and self.y1 <0:
            print(mensaje + ("3"))
        else:
            print(mensaje + ("4"))

    def vector(self,x2=0,y2=0):
        self.x2 = x2
        self.y2= y2
        a= self.x2 - self.x1
        x= self.y2 - self.y1
        v= (a,x)
        print(f"El vector es: {v}")
    
    def distancia(self,x3 =0,y3=0):
        self.x3 = x3
        self.y3=y3
        distancia = math.sqrt((self.x3-self.x1)**2+(self.y3-self.y1)**2)
        print(f"La distancia es: {distancia}")

class Rectangulo:
    #aqui recibo las tuplas
    def __init__(self,pI,pF):
        self.pI=  pI
        self.pF = pF
    
    def __str__(self):
        return (f"Los puntos ingresados son: {self.pI} y {self.pF}")
    # En esta parte utilizo algunos datos de la tuplas como son x1 de pI y x2 pF
    def base(self):
        x1= self.pI[0]
        x2= self.pF[0]
        return(x2-x1)
    #Utilizo los datos de las tuplas necesarios
    def altura(self):
        y1= self.pI[1]
        y2= self.pF[1]
        return(y2-y1)
        
    def area(self):
        #Utilizo la base y la altura del mismo objeto para obtener el area
        b= self.base()
        a= self.altura()
        return (b*a)
        
a= Punto("A",1,2)
b= Punto("B",4,5)
c= a.cordenada()
#obtenemos las tuplas del punto a y b por medio del metodo cordenada(las tuplas contienen los valores de (x1,y1) y (x2,y2))
r= Rectangulo(a.cordenada(),b.cordenada())
print(r)
print(f"La base es: {r.base()}")
print(f"La altura es: {r.altura()}")
print(f"El area es: {r.area()}")