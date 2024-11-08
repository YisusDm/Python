x = int(input("Ingrese el valor de X: "))
y = 1/(x+(1/(x+(1/(x+(1/x))))))
print(y)
operacion_1 = x + (1/x)
operacion_2 = x+(1/operacion_1)
operacion_3 = x+(1/operacion_2)
z = 1/operacion_3
print(z)