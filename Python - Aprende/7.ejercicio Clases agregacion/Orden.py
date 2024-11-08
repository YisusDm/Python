from Producto import Producto
#importamos de nuestro archivo o modulo Producto.py la clase Producto porque vamos a utilizar nuestra clase producto aqui en este modulo Orden.py
#para poder crear los objetos de las lineas 36 y 37
class Orden:
    contador_ordenes = 0

    def __init__(self, productos):#recibe el parametro productos que es la lista de objetos de tipo Producto
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)#almacena la lista de productos que recibimos
                          #para asegurarnos que nuestro parametro es una lista utilizamos list, hubiesemos podido asignarlo directamente sin el metodo list
    
    def agregar_producto(self, producto):#metodo para agregar productos de manera independiente es decir agregar el producto despues de crear nuestra objeto orden
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:#for aplicado a nuestra lista de productos linea 10
            #total += producto._precio#objeto producto atributo _precio, sin embargo al estar dentro de otra clase llamandolo de esta forma seria una mala practica
                                    # aunque tenemos acceso directamente al atributo lo correcto es
                                    # crear nuestro metodo get en Producto para el atributo encapsulado precio
                                    #ahora ya creado el metodo get ya no vamos a utilizar la instruccion 19 sino directamente la propiedad linea 20:
            total += producto.precio #a traves del metodo get definido en Producto
        return total

    def __str__(self):#convertir todos nuestros productos a un string
        productos_str = ''#almacenamos la lista de productos
        for producto in self._productos:#_producto es un atributo de esta misma clase Orden que es nuestra lista creada en esta misma clase Orden
            productos_str += producto.__str__() + '|' # producto.__str__() --> estamos mandando a llamar al metodo __str__ de Producto

        return f'Orden: {self._id_orden}, \nProductos: {productos_str}' #retornamos la orden con sus respectivos productos


#como vamos a ejecutar unas pruebas dentro de este mismo modulo lo verificamos con:
if __name__ == '__main__':
    
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalón', 150.00)
    productos1 = [producto1, producto2]#creamos nuestra lista a partir de los productos creados
    orden1 = Orden(productos1)#una vez ya tenemos nuestra lista de productos entonces creamos nuestro objeto de Orden y le pasamos nuestra lista de productos a su constructor de Orden
    print(orden1)
    orden2 = Orden(productos1) #creamos una segunda orden de momento con los mismos productos de la orden 1
    print(orden2)
