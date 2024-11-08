import re

entrada = "(10.0, 25.0, 0.0)"

# Utilizar expresión regular para extraer las coordenadas
coincidencia = re.match(r"\((-?\d+\.\d+), (-?\d+\.\d+), (-?\d+\.\d+)\)", entrada)

if coincidencia:
    x = float(coincidencia.group(1))
    y = float(coincidencia.group(2))
    # z = float(coincidencia.group(3))  # Si necesitas también la coordenada z

    print("Coordenada x:", x)
    print("Coordenada y:", y)
    # print("Coordenada z:", z)  # Descomenta si necesitas también la coordenada z
else:
    print("Entrada no válida.")
