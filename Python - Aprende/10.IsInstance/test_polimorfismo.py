from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())#objeto apunta a un objeto de tipo empleado que es lo que hacemos en la inst 16
    #en este caso se manda a llamar el metodo __str__ de la clase padre
    #cuando se ejecute la inst 21 el objeto que recibimos es una referencia que apunta a un objeto de la clase Gerente
    # y en ese caso se manda a llamar al metodo __str__ de la clase Gerente
   
   
   
    #print(objeto.departamento)#esta instruccion nos daria un error
    #ya que un objeto de tipo Empleado no contiene
    # no contiene el atributo departamento el cual unicamente se ha definido en la clase Gerente, entonces para solucionarlo:
    if isinstance(objeto, Gerente):#si el objeto que recibimos es una instancia de la clase Grente, entonces accedemos a su atributo
        print(objeto.departamento)


empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)
