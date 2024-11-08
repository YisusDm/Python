#se importan Persona y Empresa pára crear obj de estas clases y luego pasarselos a la clase banco
from Persona  import Persona
from Empresa  import Empresa

class Banco:
    # se definen 2 atributos de clase
    _clientes=[]
    _numeroClientes=0
    #se crea el contructor y se inicializa el atributo 
    def __init__(self,nombreBanco):
        self._nombreBanco = nombreBanco
    #get de _nombreBanco
    def obtNombreBanco(self):
        return self._nombreBanco
    #metodo para cambiar dicho nombre dle banco
    def cambiarNombreBanco(self , nombre):
        self._nombreBanco = nombre
    #metodo para agregar cliente
    def addCliente(self,clientes):        
        #se crea un bucle que me recorre la cantidad de clientes que tengo en mi parametro clientes gracias a Len()
        for i in range(len(clientes)):
            #se guardan los objetos quee tiene mi parametro cliente en dichas posiciones
            self._clientes.append(clientes[i])
            #se incrementa  _numeroClientes para saber cuanto clientes tiene el banco
            self._numeroClientes+=1
    # get de _numeroClientes            
    def obtNumClientes(self):
        return self._numeroClientes
    def getClientes(self): 
        #se definen unass variables de tipo listay dicionarios las cuales sirven para algunas peticiones como (El nombre de todos los clientes,etc..) luego se retornan en una cadena formateada               
        NombreClientes=[]
        CedulaPersonas=[]
        DatosEmpresa={}
        NombreClientesMenores=[]
        ClienteMasJoven={"nombre":"", "edad":1000}
        ClienteMasViejo={"nombre":"", "edad":0}

        #se crea un bucle parra recorrer todo los clientes que el banco tiene
        for i in range(self._numeroClientes):

            #se atarapa el nombre de la clase para diferenciar entre Persona y Empresa (esto mas que todo se hace para separar las funciones que hace empresa y persona ya que la empresa me retorna el nombre de la empresa y el representante etc..)            
            
            NombreClase=type(self._clientes[i]).__name__
            
            if  NombreClase == "Empresa" :
                #se guardan los nombres de todos lo clientes tipo empresa ( en esta parte no es necesesario separar los nombre de clientes de personas con empresas debido a que ambos son clientes)
                NombreClientes.append(self._clientes[i].obtNombre())
                #se guardan en un dicionario el nombre de la empresa y el representante de dicha empresa
                DatosEmpresa[f"{self._clientes[i].obtNombre()}"]= self._clientes[i].obtRepresentante()

            elif NombreClase == "Persona":
                #se guarda el nombre de los clientes tipo persona y la identificacion
                NombreClientes.append(self._clientes[i].obtNombre())            
                CedulaPersonas.append(self._clientes[i].obtIdentificacion())
                
                #se hace un if para saber cuales son los nombre de los clientes menores de edad y estos se guardan en una lista
                if self._clientes[i].obtEdad()<18 :
                
                    NombreClientesMenores.append(self._clientes[i].obtNombre())                        
                #se hace otro if para saber cual es  el cliente mas joven  y estos datos como nombre se guardan en un dicionarios
                if  ClienteMasJoven["edad"]>self._clientes[i].obtEdad():
                
                    ClienteMasJoven["nombre"]=self._clientes[i].obtNombre()
                    ClienteMasJoven["edad"]=self._clientes[i].obtEdad()
                #se hace otro if para saber cual es  el cliente mas viejo  y estos datos como nombre se guardan en un dicionarios
                if  ClienteMasViejo["edad"]<self._clientes[i].obtEdad():
                    ClienteMasViejo["nombre"]=self._clientes[i].obtNombre()
                    ClienteMasViejo["edad"]=self._clientes[i].obtEdad()

            else:
                print("huboun error el objeto no pertenece a ninguna clase")
            
        #se formatea el mensaje que debe salir por consola
        return (
            f"los nombre de todos los clientes son: {NombreClientes}\n"\
            f"los datos de las empresa son: {DatosEmpresa}\n"\
            f"Los clientes menores de edad son : {NombreClientesMenores}\n"\
            f"El cliente mas joven es: {ClienteMasJoven}\n"\
            f"EL cliente mas viejo es: {ClienteMasViejo}"            
        )
    #se crea el metodo buscar cliente 
    def buscarCliente(self,posicion):
        if posicion>len(self._clientes):
            print("no existe tal registro")
        else:
            return(self._clientes[posicion])            
persona1 =Persona(111,18,"jose#1")
persona2 =Persona(112,1,"jose#2")
persona3 =Persona(113,12,"jose#3")
persona4 =Persona(114,95,"jose#4")
persona5 =Persona(115,66,"jose#5")
persona6 =Persona(116,0,"jose#6")
clientes=[]
clientes.append(persona1)
clientes.append(persona2)
clientes.append(persona3)
clientes.append(persona4)
clientes.append(persona5)
clientes.append(persona6)
empresa1=Empresa(11124,"thanos.com","mario")
empresa2=Empresa(11124,"its mario","luigi")
empresa1.cambiarRepresentante("browser")
clientes.append(empresa1)
clientes.append(empresa2)


#print(classe)
banquito=Banco("miami")
banquito.addCliente(clientes)

print(banquito.getClientes())




