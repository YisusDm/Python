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
    NombreClientes=[]
    CedulaPersonas=[]
    DatosEmpresa=[]
    DatosPersonas=[]
    NombreClientesMenores=[]
    ClienteMasJoven={"Nombre":"","Edad":1000}
    ClienteMasViejo={"Nombre":"","Edad":0}

    def __init__(self,nombreBanco):
        self._nombreBanco=nombreBanco

    def __str__(self):
        print("los nombre de todos los clientes son: ")
        for i in range(len(self.NombreClientes)):
            print(f"{i+1}: {self.NombreClientes[i]}")
        print("los datos de los clientes tipo (persona) son: ")
        for i in range(len(self.DatosPersonas)):
            print (f"{i+1}: {self.DatosPersonas[i]}\n")
        print("los datos de los clientes tipo (empresa) son: ")
        for i in range(len(self.DatosEmpresa)):
            print (f"{i+1}: {self.DatosEmpresa[i]}\n")
        print("Los clientes menores de edad son: ")
        for i in range(len(self.NombreClientesMenores)):
            print (f"{i+1}: {self.NombreClientesMenores[i]}\n")
        print(f"El cliente mas joven es: {self.ClienteMasJoven}\n")
        print(f"EL cliente mas viejo es: {self.ClienteMasViejo}")

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
        for i in range(self._numeroClientes):
            NombreClase=type(self._clientes[i]).__name__
            if  NombreClase == "Empresa" :
                self.NombreClientes.append(self._clientes[i].obtNombre())
                Dic={"Nit":self._clientes[i].obtIdentificacion(),"Cliente":self._clientes[i].obtNombre(),"Representante":self._clientes[i].obtRepresentante()}
                self.DatosEmpresa.append(Dic)
            elif NombreClase == "Persona":
                self.NombreClientes.append(self._clientes[i].obtNombre())            
                self.CedulaPersonas.append(self._clientes[i].obtIdentificacion())
                DicC={"Cedula":self._clientes[i].obtIdentificacion(),"Nombre":self._clientes[i].obtNombre()}
                self.DatosPersonas.append(DicC)
                
                if (self._clientes[i].obtEdad())<18 :
                    self.NombreClientesMenores.append(self._clientes[i].obtNombre())                        
                if  self.ClienteMasJoven["Edad"]>self._clientes[i].obtEdad():
                    self.ClienteMasJoven["Nombre"]=self._clientes[i].obtNombre()
                    self.ClienteMasJoven["Edad"]=self._clientes[i].obtEdad()
                
                if  self.ClienteMasViejo["Edad"]<self._clientes[i].obtEdad():
                    self.ClienteMasViejo["Nombre"]=self._clientes[i].obtNombre()
                    self.ClienteMasViejo["Edad"]=self._clientes[i].obtEdad()

            else:
                print("upsss hubo error el objeto no pertenece a ninguna clase")
            
    def buscarCliente(self,posicion):
        if posicion>len(self._clientes):
            print("no existe tal registro")
        else:
            return(self._clientes[posicion])

    _numeroClientes=int(input("Ingrese el numero de clientes: "))
    for i in range(_numeroClientes):
        tipoCliente=int(input("Ingrese el tipo de Cliente: \n>>(1) para Empresa\n>>(2) para Persona \nSeleccione: "))
        nom=input("Ingrese el nombre del cliente: ")
        if(tipoCliente==1):
            nit=input("Ingrese el nit de la empresa: ")
            r=input("Ingrese el nombre del representante: ")
            empresa=Empresa(nom,nit,r)
            _clientes.append(empresa)
        else:
            ced=input("Ingrese su numero de cedula: ")
            ed=int(input("Ingrese la edad: "))
            persona=Persona(nom,ced,ed)
            _clientes.append(persona)
    

#Start
banco=Banco("BancoReDSena")
banco.getClientes()
print(banco.__str__())


