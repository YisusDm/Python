def analizar_temperaturas():
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Solicitar temperaturas al usuario y validarlas
    for dia in dias_semana:
        while True:
            temperatura = float(input(f"Ingrese la temperatura promedio para {dia}: "))
            if temperatura > 0: # Validacion numeros positivos (mayores que cero)
                temperaturas.append(temperatura)
                break
            else:
                print("La temperatura debe ser un número positivo. Intente nuevamente.")

    # Calcular
    promedio_pares = sum(temperaturas[i] for i in range(1, 7, 2)) / len(temperaturas[1::2])  # Martes (1), Jueves(3), Sábado(5)
    promedio_impares = sum(temperaturas[i] for i in range(0, 7, 2)) / len(temperaturas[::2])  # Lunes(0), Miércoles(2), Viernes(4), Domingo(6)
    suma_potencias = sum(temp**7 for temp in temperaturas)

    # Mostrar resultados
    print("\nResultados:")
    print(f"Promedio de temperaturas en días pares: {promedio_pares:.2f}")
    print(f"Promedio de temperaturas en días impares: {promedio_impares:.2f}")
    print(f"Suma de temperaturas elevadas a la 7ma potencia: {suma_potencias:.2f}")

# Ejecutar la función
analizar_temperaturas()