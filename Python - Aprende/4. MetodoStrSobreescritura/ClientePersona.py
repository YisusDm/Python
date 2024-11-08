from Persona import * #importamos las clases de nuestro modulo Persona.py

persona1 = Persona('Juan', 28)
#print(persona1.__str__())#no es necesario utilizar esta sintaxis pues
                         #la llamada a este metodo magico se realiza de 
                         # manera automatica,entonces:
print(persona1)
empleado1 = Empleado('Karla', 30, 5000)#objeto de tipo empleado
print(empleado1)