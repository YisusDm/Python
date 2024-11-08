# def tabla(num,terminos=20):
#     for x in range(terminos):
#         n=x*num
#         # añadimos los parametros sep y end a la funcion print
#         # con sep podemos añadir un caracter separando cada elemento, en este caso separaría
#         # el valor de n con la ","
#         # con end incluimos un caracter al final de la impresión
#         # esto también es útil para mostrar todos los datos en una única linea
#         print(n,",",sep="",end="")
#     print()
    
# tabla(4)
 

# creamos una función para cargar los datos
# def cargar(total):
#     lista=[]
#     for x in range(total):
#         num=int(input("Ingrese un valor entero: "))
#         lista.append(num)
#     return lista
 
 
# # creamos una función para separar las listas de numeros positivos y negativos
# def separar(lista):
#     pos=[]
#     neg=[]
#     for x in range(len(lista)):
#         if lista[x]>=0:
#             pos.append(lista[x])
#         else:
#             neg.append(lista[x])
#     return [pos,neg]
 
 
# # declaramos una tercera función para imprimir los valores
# def imprimir(mensaje,lista):
#     print("-"*10)   
#     print(mensaje)
#     print(lista)
#     print("-"*10)
 
 
# # bloque principal
# lista=cargar(10)
# pos,neg=separar(lista)
# imprimir("Imprimimos la lista original",lista)
# imprimir("Imprimimos la lista de numeros positivos",pos)
# imprimir("Imprimimos la lista de numeros negativos",neg)








#Parametros por defecto

# def titulo_subrayado(titulo,caracter="-"):
#     print(titulo)
#     print(caracter*len(titulo))
 
 
# # bloque principal
# titulo_subrayado("Hola mundo")
# titulo_subrayado("Cambiando el valor opcional","*")



# def cantidad_mayores(edad,*edades):
#     cant=0
#     print(edad)
#     if edad>=18:
#         cant=cant+1
#     for x in range(len(edades)):
#         if edades[x]>=18:
#             cant=cant+1
#     return cant
 
 
# # bloque principal
# print("La cantidad de personas mayores a 18 son:", cantidad_mayores(5,18,21,47,16,32))
# print("La cantidad de personas mayores a 18 son:", cantidad_mayores(22,17,32,8,24))
# print("La cantidad de personas mayores a 18 son:", cantidad_mayores(45,12,25,8,19))


# dni="91262455"
# dniLista=list(dni)
# print(dniLista[:3])


# lista=[]
# for i in range(1, 25):
#     if (i%7==0):    	 	
#         lista.append(str(i))
# print (' '.join(lista))

# class Ejemplo:
#     def __metodo_privado(self):
#         print("soy un metodo inalcanzable dede fuera")
# e=Ejemplo()
# e.__metodo_privado()

###########################################################################
###########################################################################

# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad

#     def mostrar_detalle(self):
#         print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

# persona1 = Persona('Juan', 'Perez', 28)
# persona1.mostrar_detalle()
# persona1.telefono = '55441122'
# print(persona1.telefono)
# # Persona.mostrar_detalle(persona1)

# persona2 = Persona('Karla', 'Gomez', 30)
# persona2.mostrar_detalle()
# print(persona2.telefono)



##################################################################


# class Cubo:
#     def __init__(self, ancho, alto, profundo):
#         self.ancho = ancho
#         self.alto = alto
#         self.profundo = profundo

#     def calcular_volumen(self):
#         return self.ancho * self.alto * self.profundo

# ancho = int(input('Proporciona el ancho: '))
# alto = int(input('Proporciona el alto: '))
# profundo = int(input('Proprociona lo profundo: '))

# cubo1 = Cubo(ancho, alto, profundo)
# print(f'Volúmen cubo: {cubo1.calcular_volumen()}')



################################33333

# class Aritmetica:
#     """
#     Clase Aritmetica para realizar las operaciones de sumar, restar, etc
#     """
#     def __init__(self, operandoA, operandoB):
#         self.operandoA = operandoA
#         self.operandoB = operandoB

#     def sumar(self):
#         return self.operandoA + self.operandoB

#     def restar(self):
#         return self.operandoA - self.operandoB

#     def multiplicar(self):
#         return self.operandoA * self.operandoB

#     def dividir(self):
#         return self.operandoA / self.operandoB

# aritmetica1 = Aritmetica(5,3)
# print(f'Suma: {aritmetica1.sumar()}')
# print(f'Resta: {aritmetica1.restar()}')
# print(f'Multiplicación: {aritmetica1.multiplicar()}')
# #print(f'División: {aritmetica1.dividir():.2f}') #ok redondeo
# print('División: {:.2f}'.format(aritmetica1.dividir())) #ok redondeo

##############################################################################33
# class Persona:
#     ##recordar que los parametros para tuplas *valores y diccionarios **terminos son 
#     # opcionales no obligatorios     # por eso en la persona2 no es obligatorio enviarlos
#     def __init__(self, nombre, apellido, edad, *valores, **terminos):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.valores = valores
#         self.terminos = terminos

#     def mostrar_detalle(self):
#         print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

# persona1 = Persona('Juan', 'Perez', 28, '44553322', 2, 3, 5, m='manzana', p='pera')
# persona1.mostrar_detalle()

# persona2 = Persona('Karla', 'Gomez', 30)
# persona2.mostrar_detalle()









#################   ENCAPSULAMIENTO ############################################3

# class Ejemplo:
#     _atributo_privado = "Soy un atributo inalcanzable desde fuera."

#     def _metodo_privado(self):
#         print("Soy un método inalcanzable desde fuera.")

#     def atributo_publico(self):
#         return self._atributo_privado

#     def metodo_publico(self):
#         return self._metodo_privado()

# e = Ejemplo()
# print(e.atributo_publico())
# print(e._atributo_privado)# aunque aun asi lo podemos acceder
# e.metodo_publico()








# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self._nombre = nombre
#         self.apellido = apellido
#         self.edad = edad

#     def mostrar_detalle(self):
#         print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

# persona1 = Persona('Juan', 'Perez', 28)
# persona1._nombre = 'Juan Carlos' # no es lo recomendado
# persona1.mostrar_detalle()

# podemos utilizar no un solo guion bajo sino dos guiones bajos al inicio de nuestro
# atributo para restringir este tipo de situaciones como el de la linea 243
#para no permitir modificar un atributo fuera de la clase:

# class Persona:
#         def __init__(self, nombre, apellido, edad):
#             self.__nombre = nombre
#             self.apellido = apellido
#             self.edad = edad

#         def mostrar_detalle(self):
#             print(f'Persona: {self.__nombre} {self.apellido} {self.edad}')

# persona1 = Persona('Juan', 'Perez', 28)
# persona1.__nombre = 'Juan Carlos' # no es lo recomendado osea lo mas utilizado es con 
# # un solo guion bajo # fijense que no hace la modificacion de esta forma
# persona1.mostrar_detalle()


#pero si queremos restringir el acceso para que no se pueda modificar directamente 
# ese atributo #para ello vamos a utilizar los conocidos metodos set y get

# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self._nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#     #estamos indicando que nuestro metodo nombre va a recuperar el atributo de instancia 
#     #de clase _nombre de esta forma solo lo vamos a poder acceder a traves del metodo   
    
#     def nombre(self):
#         print("llamando metodo get nombre")
#         return self._nombre
    
   
# p1=Persona("Oscar","Gonzalez",52)
# #print(p1.nombre())# de esta forma ya no estamos accediendo directamente al atributo de nombre
#                   #pero aun asi aun lo podemos hacer:
# print(p1._nombre) # pero esto debemos evitarlo pues son encapsulados y no deberiamos accederlos
# de esta manera #y para asegurarnos de que esto no suceda entonces tenemos el
# decorador(@property)
# que basicamente modifica el comportamiento de nuestro metodo:





# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self._nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#     #estamos indicando que nuestro metodo nombre va a recuperar el atributo de instancia 
#     #de clase _nombre de esta forma solo lo vamos a poder acceder a traves del metodo   
#     #el decorador nos va permitir acceder al metodo como si fuera un atributo por eso no hacemos 
#               # print(p1.nombre()) linea 309
#     @property 
#     def nombre(self):
#         print("llamando metodo get nombre")
#         return self._nombre
    
   
# p1=Persona("Oscar","Gonzalez",52)
# print(p1.nombre) # directamente accedemos al atributo privado de manera indirecta accediendolo como si fuera
                   #un atributo de nuestra clase, si le pongo los parentesis da un error



#ahora para modificar el atributo protegido a traves del metodo setter:

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        print('Llamando método get nombre')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

p1 = Persona('Oscar', 'Gonzalez', 28)
#print(p1.nombre) #llamado al metodo get antes de la modificacion
# p1.nombre('Oscar Mauricio') #ya no es necesario hacerlo asi como un metodo pues desde 
# el decorador ya estamos indicando cual va a ser el atributo a modificar, sino asi:
#p1.nombre = 'Oscar Mauricio'#esto hace llamar de manera indirecta al metodo nombre 
# pasando el valor string "Oscar Mauricio" al parametro el cual es asignado al 
# atributo de instancia #posteriormente mandamos a llamar a nuestrometodo get para notar 
# el cambio:
#print(p1.nombre) #llamado al metodo get despues de la modificacion

# de la forma anterior ya vamos a poder evitar hacer lo de la linea 347:
#print(p1._nombre)
#p1._nombre = 'Cambio' #aunque aun se puede hacer  estariamos indicando que desconocemos python 
#print(p1._nombre) 
#lo suyo seria:
#p1.nombre = 'Cambio2'
#print(p1.nombre)


#AtributosReadOnly:
#si queremos evitar este tipo de instrucciones p1.nombre = 'Cambio2'
# entonces quitamos el metodo sett y de esta forma el atributo nombre seria de solo lectura ya que no podemos modificar su valor al no tener un metodo setter
#aunque se podria como mala practica hacerlo asi:



# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self._nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
     
#     @property
#     def nombre(self):
#         print("llamando metodo get nombre")
#         return self._nombre
    
    
# p1=Persona("Oscar","Gonzalez",52)
# p1.nombre = 'Cambio2'
# print(p1.nombre) # nos daria un error de tipo: can't set attribute

# se podria hacer con malas practicas recuerden de esta forma que debemos evitar:

# p1=Persona("Oscar","Gonzalez",52)
# p1._nombre = 'Cambio2'
# print(p1._nombre)











# completndo los demas atributo:
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self._nombre = nombre
#         self._apellido = apellido
#         self._edad = edad

#     @property
#     def nombre(self):
#         return self._nombre

#     @nombre.setter
#     def nombre(self, nombre):
#         self._nombre = nombre

#     @property
#     def apellido(self):
#         return self._apellido

#     @apellido.setter
#     def apellido(self, apellido):
#         self._apellido = apellido

#     @property
#     def edad(self):
#         return self._edad

#     @edad.setter
#     def edad(self, edad):
#         self._edad = edad

#     def mostrar_detalle(self):
#         print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

# persona1 = Persona('Oscar', 'Gonzalez', 52)
# persona1.nombre = 'Oscar Mauricio'
# persona1.apellido = 'Gomez'
# persona1.edad = 50
# persona1.mostrar_detalle()



