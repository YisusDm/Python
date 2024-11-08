# b. Escriba un programa que reciba como entrada una palabra o una frase en minúsculas y conserve solamente la primera aparición de cada letra, eliminando sus apariciones posteriores. Tenga en cuenta que letras tildadas se diferencias de las que no lo están.

from collections import OrderedDict
# entrada: Maratón de programación Sena
# Salida: martón de pogc s

entrada ="Maratón de programación Sena"
#entrada = input("Escriba aqui: ") 
entradaMin = entrada.lower()
print(entradaMin)
print("".join(OrderedDict.fromkeys(entradaMin)))