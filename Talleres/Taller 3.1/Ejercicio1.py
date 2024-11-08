from tabulate import tabulate

table1 = []
table2 = []

cabezera=["Casa", "Max", "Promedio", "Tipo"]
table2.insert(0, cabezera)

maxProm = 0
usuariosSuperan = 0

usuarios = int(input("¿Cuantos usuarios vas a ingresar? "))
maximoPermitido = int(input("Ingrese el maximo permitido: "))
for i in range(usuarios):
  print("Usuario", i+1)

  
  consumoTotalUsuario = 0
  maxConsumo = 0
  tipo = 0
  casa = input("Ingrese el la casa: ")

  for ii in range(3):
    print("Mes", ii + 1)
    consumo = int(input("Ingrese el consumo de este mes: "))
    consumoTotalUsuario += consumo
    if consumo > maxConsumo:
      maxConsumo = consumo
  
  promedioUsuario = consumoTotalUsuario / 3

  if promedioUsuario > maximoPermitido:
    tipo = 1
    usuariosSuperan += 1
    maxProm += maxConsumo

  table1.insert(0, casa)
  table1.insert(1, maxConsumo)
  table1.insert(2, f"{promedioUsuario:,.2f}")
  table1.insert(3, tipo)
  table2.insert(i+1, table1)
  table1 = []
  print(maxProm)

maxProm = maxProm / usuariosSuperan
porcentajeNoSuperan = 100 * ((usuarios - usuariosSuperan) / usuarios)

print(tabulate(table2))
print(f"Max promediado que superan el tope:{maxProm:,.2f}")
print(f"Porcentaje de casa que no superan tope: {porcentajeNoSuperan:,.2f}%")