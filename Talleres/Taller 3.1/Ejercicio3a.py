#a. La codificación de una palabra se realiza poniendo al #final de la palabra la letra,inicial(eliminado esta), y añadiendo la letra “a”a modo de terminación.Así, por ejemplo, para la palabra “casa” el resultado sería: asaca.Realice un programa en Python que reciba por teclado 5 frases y codifique cada una de sus palabras a través de este método de codificación de palabras.

cadena = input("Ingrese una frase: ")
contador = cadena.count(" ")
contador = contador + 1
#print(contador)
for i in range(contador):
  i = cadena.split(" ")[i]
  #print(i)
  palabra = i
  palabra1 = palabra[1:len(palabra)] + palabra[0] +"a"
  print (palabra1, end=" ")