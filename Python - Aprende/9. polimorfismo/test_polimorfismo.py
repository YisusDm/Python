from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):#va a imprimir el detalle de los objetos empleado o gerente
    #es decir va a ejecutar el metodo __str__ de cualquiera de los objetos
    # print(objeto) #polimorfismo
    print(type(objeto))#para saber cual es la clase del objeto al cual estamos apuntando
    print(objeto.mostrar_detalles())

empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)