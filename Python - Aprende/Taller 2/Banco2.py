from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self,nom):
        self._nombre=nom
    def obtNombre(self):
        return self._nombre 
    @abstractmethod       
    def obtIdentificacion():
        pass

class Empresa(Cliente):
    def __init__(self,nom,nit,r):
        super().__init__(nom)
        self._nit=nit
        self._representante=r
    def obtIdentificacion(self):
        return self._nit
    def obtRepresentante(self):
        return self._representante
    def cambiarRepres(self,repres):
        self._representante=repres
    


class Persona(Cliente):
    def __init__(self,nom,ced,ed):
        super().__init__(nom)
        self._cedula=ced
        self._edad=ed
    def obtIdentificacion(self):
        return self._cedula
    def obtEdad(self):
        return self._edad
    def cumpleaños(self):
        self._edad+=1

class Banco:
    _clientes=[]
    _numeroClientes=0
    def __init__(self,nombreBanco):
        self._nombreBanco=nombreBanco
    def obtnombreBanco(self):
        return self._nombreBanco
    def cambiarNombre(self,nombreBanco):
        self._nombreBanco=nombreBanco
    def addCliente(self,clientes):
        for i in range(len(clientes)):
            self._clientes.append(clientes[i])
            self._numeroClientes+=1
    def obtnumClientes(self):
        return self._numeroClientes
    def getClientes(self):
        NombreClientes=[]
        CedulaPersonas=[]
        DatosEmpresa=[]
        DatosPersonas=[]
        NombreClientesMenores=[]
        ClienteMasJoven={"Nombre":"","Edad":1000}
        ClienteMasViejo={"Nombre":"","Edad":0}
        for i in range(self._numeroClientes):
            NombreClase=type(self._clientes[i]).__name__
            if  NombreClase == "Empresa" :
                NombreClientes.append(self._clientes[i].obtNombre())
                Dic={"Cliente":self._clientes[i].obtNombre(),"Representante":self._clientes[i].obtRepresentante()}
                DatosEmpresa.append(Dic)
            elif NombreClase == "Persona":
                NombreClientes.append(self._clientes[i].obtNombre())            
                CedulaPersonas.append(self._clientes[i].obtIdentificacion())
                DicC={"Cedula":self._clientes[i].obtIdentificacion(),"Nombre":self._clientes[i].obtNombre()}
                DatosPersonas.append(DicC)
                
                if self._clientes[i].obtEdad()<18 :
                    NombreClientesMenores.append(self._clientes[i].obtNombre())                        
                if  ClienteMasJoven["Edad"]>self._clientes[i].obtEdad():
                    ClienteMasJoven["Nombre"]=self._clientes[i].obtNombre()
                    ClienteMasJoven["Edad"]=self._clientes[i].obtEdad()
                
                if  ClienteMasViejo["Edad"]<self._clientes[i].obtEdad():
                    ClienteMasViejo["Nombre"]=self._clientes[i].obtNombre()
                    ClienteMasViejo["Edad"]=self._clientes[i].obtEdad()

            else:
                print("upsss hubo error el objeto no pertenece a ninguna clase")
            
        return (
            f"los nombre de todos los clientes son: {NombreClientes}\n"\
            f"los datos de las personas son: {DatosPersonas}\n"\
            f"los datos de las empresa son: {DatosEmpresa}\n"\
            f"Los clientes menores de edad son : {NombreClientesMenores}\n"\
            f"El cliente mas joven es: {ClienteMasJoven}\n"\
            f"EL cliente mas viejo es: {ClienteMasViejo}"            
        )
    def buscarCliente(self,posicion):
        if posicion>len(self._clientes):
            print("no existe tal registro")
        else:
            return(self._clientes[posicion])

persona1 =Persona("jose#1",111,18)
persona2 =Persona("jose#2",112,15)
persona3 =Persona("jose#3",113,12)
persona4 =Persona("jose#4",114,95)
persona5 =Persona("jose#5",115,66)
persona6 =Persona("jose#6",116,13)
clientes=[]
clientes.append(persona1)
clientes.append(persona2)
clientes.append(persona3)
clientes.append(persona4)
clientes.append(persona5)
clientes.append(persona6)
empresa1=Empresa("thanos.com",11124,"mario")
empresa2=Empresa("its mario",11124,"luigi")
empresa1.cambiarRepres("browser")
clientes.append(empresa1)
clientes.append(empresa2)


#print(classe)
banquito=Banco("miami")
banquito.addCliente(clientes)

print(banquito.getClientes())