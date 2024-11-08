from tabulate import tabulate

# Datos de ejemplo
data = [["Alice", 24, "Engineer"],
        ["Bob", 30, "Doctor"],
        ["Charlie", 22, "Artist"]]

# Tabla en formato predeterminado
print(tabulate(data, headers=["Name", "Age", "Occupation"], tablefmt="pretty"))

# Tabla en formato "grid"
print(tabulate(data, headers=["Name", "Age", "Occupation"], tablefmt="grid"))

# Tabla en formato "html"
print(tabulate(data, headers=["Name", "Age", "Occupation"], tablefmt="html"))

# Tabla en formato "latex"
print(tabulate(data, headers=["Name", "Age", "Occupation"], tablefmt="latex"))

# Tabla en formato "mediawiki"
print(tabulate(data, headers=["Name", "Age", "Occupation"], tablefmt="mediawiki"))
