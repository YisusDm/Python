import os
import sqlite3
import json
from tqdm import tqdm


def BuscarNumeroDocumento():
    # Carpeta donde se guardarán los JSON
    carpeta_json = "Json"

    # Nombre de la base de datos SQLite
    nombre_base_datos = "Backup.db3"

    BaseDatos = input("Ingrese el Nombre de la Base De Datos que se va a Usar: ").strip()
    nombre_base_datos = BaseDatos.replace(" ","")+'.db3'


    
    if os.path.isfile(nombre_base_datos): # Comprueba si la base de datos ya existe antes de conectarte
        
        # Obtener los números de documento ingresados por consola (separados por coma)
        numeros_documento_input = input("Ingresa los números de documento separados por coma: ")
        numeros_documento = [numero.strip() for numero in numeros_documento_input.split(",")]

        # Crear la carpeta Json si no existe
        if not os.path.exists(carpeta_json):
            os.makedirs(carpeta_json)

        # Eliminar archivos JSON existentes en la carpeta
        for archivo_existente in os.listdir(carpeta_json):
            archivo_completo = os.path.join(carpeta_json, archivo_existente)
            if os.path.isfile(archivo_completo):
                os.remove(archivo_completo)      

        # Inicializar listas para almacenar los JSON y contar su número
        json_resultados = []
        numero_json = len(numeros_documento)

        try:      # Conectar a la base de datos SQLite
            conexion = sqlite3.connect(nombre_base_datos, check_same_thread=False)
            cursor = conexion.cursor()

            # Crear una barra de progreso global
            with tqdm(total=numero_json, desc="Procesado") as pbar:
                # Generar y guardar los JSON para cada número de documento
                for numero_documento in numeros_documento:
                    # Consulta SQL para obtener los datos del número de documento
                    consulta_sql = f"""
                        SELECT
                            Id,
                            CodigoEds,
                            CodigoArticulo,
                            Cara,
                            CodigoPosicion,
                            TotalSurtidor,
                            Volumen,
                            Precio,
                            ROM,
                            Placa,
                            TramaID,
                            Estado,
                            SectorVenta,
                            IdentificacionVendedor,
                            NumeroDocumento,
                            TipoVenta,
                            IdTurno,
                            IdVentaTI,
                            LecturaInicial,
                            LecturaFinal,
                            WebID,
                            Km,
                            NombreResponsable,
                            FechaInicial,
                            FechaFin
                        FROM FinDeVentaLocal
                        WHERE NumeroDocumento = '{numero_documento}'
                    """
                    
                    # Ejecutar la consulta SQL
                    cursor.execute(consulta_sql)
                    
                    # Obtener los nombres de las columnas
                    columnas = [descripcion[0] for descripcion in cursor.description]
                    
                    # Obtener los datos del número de documento
                    datos_documento = cursor.fetchone()
                    
                    # Verificar si se encontraron datos para el número de documento
                    if datos_documento:
                        # Crear un diccionario con la estructura deseada
                        resultado = {
                            "id": datos_documento[0],
                            "codigoEds": datos_documento[1],
                            "codigoArticulo": datos_documento[2],
                            "Cara": datos_documento[3],
                            "codigoPosicion": datos_documento[4],
                            "totalSurtidor": datos_documento[5],
                            "volumen": datos_documento[6],
                            "precio": datos_documento[7],
                            "ROM": datos_documento[8],
                            "placa": datos_documento[9],
                            "tramaID": datos_documento[10],
                            "Estado": 3,  # Valor predeterminado "Estado" como 3
                            "sectorVenta": datos_documento[12],
                            "identificacionVendedor": datos_documento[13],
                            "NumeroDocumento": datos_documento[14],
                            "tipoVenta": datos_documento[15],
                            "idTurno": datos_documento[16],
                            "idVentaTI": datos_documento[17],
                            "lecturaInicial": datos_documento[18],
                            "lecturaFinal": datos_documento[19],
                            "wId": datos_documento[20],
                            "km": datos_documento[21],
                            "nombreCliente": datos_documento[22],
                            "fInicial": datos_documento[23],
                            "fFin": datos_documento[24]
                        }
                        
                        # Agregar el JSON a la lista
                        json_resultados.append(resultado)

                        # Actualizar la barra de progreso global
                        #pbar.update(1)
                    else:
                        print(f"\nNo se encontraron datos para el número de documento {numero_documento} en la base de datos local.")

                # Verificar si el número total de JSON es Menor o igual a 10
                if numero_json <= 10:
                    for resultado in json_resultados:
                        pbar.update(1)
                        numero_documento = resultado["NumeroDocumento"]
                        # Crear el nombre del archivo JSON basado en el número de documento
                        nombre_archivo_json = os.path.join(carpeta_json, f"{numero_documento}.json")       
                        # Guardar el JSON en el archivo correspondiente
                        with open(nombre_archivo_json, "w") as archivo_json:
                            json.dump(resultado, archivo_json, indent=2)
                            print(f"JSON para el número de documento {numero_documento} guardado en '{nombre_archivo_json}'")

                # Verificar si el número total de JSON es mayor que 10
                elif  numero_json > 10:
                    # Dividir los JSON en lotes de máximo 40 elementos
                    max_elementos_por_lote = 40
                    lotes_json = [json_resultados[i:i + max_elementos_por_lote] for i in range(0, len(json_resultados), max_elementos_por_lote)]
                    for i, lote in enumerate(lotes_json):
                        pbar.set_description(f"Guardando Lote_{i + 1}")
                        for resultado in lote:
                            #numero_documento = resultado["NumeroDocumento"]
                            nombre_archivo_json = os.path.join(carpeta_json, f"Lote_{i + 1}.json")
                            with open(nombre_archivo_json, "w") as archivo_json:
                                json.dump(lote, archivo_json, indent=2)     
                        pbar.update(len(lote))    
                        print(f"\nLotes de JSON creados y guardados en la carpeta 'Json' - Lote_{i + 1}")

        except sqlite3.Error as error:
            print("Error al conectar a la base de datos SQLite:", error)
        finally:
            # Cerrar la conexión a la base de datos
            if conexion:
                conexion.close()
    else:
        print("La base de datos no existe.")





