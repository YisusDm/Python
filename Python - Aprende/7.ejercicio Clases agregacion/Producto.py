class Producto:
    contador_productos = 0 #variable de clase

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1 #incrementamos directamente nuestra variable de clase
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property #metodo get para el atributo precio
    def precio(self):
        return self._precio #retorna el atributo encapsulado precio

    def __str__(self):#para representar nuestro objeto a traves de un string
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'
        #estamos utilizando los atributos encapsulados dado que estamos en nuestra misma clase no en una clase externa
        #porque de ser asi sabemos que utilizariamos los metodos get y set

if __name__ == '__main__':# como esta clase la vamos a utilizar en otros modulos
                          #revisamos si el atributo de __name__ es igual a la clase que se esta ejecutando en este momento
                          #este codigo unicamente solo se ejecuta si solo estamos ejecutando la prueba desde nuestro mismo modulo que en nuestro caso es Producto.property
    
    #para prueba:                      
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalón', 150.00)
    print(producto2)