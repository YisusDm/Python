import time
from tqdm import tqdm

class NodoTarea:
    """Representa una tarea en la lista enlazada."""
    def __init__(self, nombre, descripcion):
        self.nombre = nombre  # Nombre corto de la tarea
        self.descripcion = descripcion  # Descripción detallada
        self.estado = "Pendiente"  # Estado inicial
        self.siguiente = None

class ListaTareas:
    """Lista enlazada simple para administrar tareas pendientes."""
    def __init__(self):
        self.primera = None

    def agregar_tarea(self, nombre, descripcion):
        """Agrega una tarea al final de la lista con estado 'Pendiente'."""
        nueva_tarea = NodoTarea(nombre, descripcion)
        if not self.primera:
            self.primera = nueva_tarea
        else:
            actual = self.primera
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea

    def completar_tarea(self):
        """Ejecuta y elimina la primera tarea de la lista."""
        if not self.primera:
            print("✅ No hay tareas pendientes.")
            return

        tarea = self.primera
        print(f"🔹 Ejecutando tarea: {tarea.nombre}")
        print(f"📌 Descripción: {tarea.descripcion}")

        # Simulación de progreso
        duracion = len(tarea.descripcion) * 0.1  # 0.1s por cada caracter
        with tqdm(total=100, desc="Procesando", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}") as pbar:
            for _ in range(100):
                time.sleep(duracion / 100)
                pbar.update(1)
        print("✅ Tarea completada exitosamente!")

        # Marcar la tarea como realizada y eliminarla
        tarea.estado = "Realizada"
        self.primera = tarea.siguiente  # Avanza al siguiente nodo

    def mostrar_tareas(self):
        """Muestra todas las tareas pendientes con su estado."""
        if not self.primera:
            print("📌 No hay tareas en la lista.")
            return

        actual = self.primera
        while actual:
            print(f"🔹 {actual.nombre} | Estado: {actual.estado}")
            print(f"   📌 {actual.descripcion}")
            actual = actual.siguiente
        print("-" * 40)

# Inicialización con tareas predefinidas
tareas = ListaTareas()
tareas.agregar_tarea("Revisar informes", "Analizar datos de ventas y rendimiento financiero")
tareas.agregar_tarea("Enviar correos", "Responder a clientes y coordinar reuniones")
tareas.agregar_tarea("Actualizar base de datos", "Ingresar registros recientes y optimizar consultas")

# Menú de interacción
while True:
    print("\n📌 Gestión de Tareas")
    print("1. Agregar nueva tarea")
    print("2. Ver tareas pendientes")
    print("3. Completar tarea")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        tareas.agregar_tarea(nombre, descripcion)
    elif opcion == "2":
        tareas.mostrar_tareas()
    elif opcion == "3":
        tareas.completar_tarea()
    elif opcion == "4":
        print("👋 Saliendo...")
        break
    else:
        print("⚠ Opción inválida, intenta nuevamente.")
