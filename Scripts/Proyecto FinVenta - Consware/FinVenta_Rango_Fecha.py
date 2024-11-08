import os
import sqlite3
import json
import time
from tqdm import tqdm


def VentaRangoFechaAviso():
    print("Recuerda que para Evitar Generar Json de ventas innecesarias.\nPodemos tomar los numero de documentos (Codigo Factura) y Cargarlos en el archivo Out.txt ")
    time.sleep(5)


def VentaRangoFecha():
    # Definimos Archivosa a Usar
    carpeta_json = "Json"
    archivo_out_txt = "out.txt"
    archivo_output_txt = "output.txt"

    # Inicializamos Variables de ingreso
    nombre_base_datos = "Backup.db3"
    fecha_inicio = '2023-01-01 00:00'
    fecha_fin = '2023-01-01 23:59'

    BaseDatos = input("Ingrese el Nombre de la Base De Datos que se va a Usar: ").strip()
    nombre_base_datos = BaseDatos.replace(" ","")+'.db3'


    if os.path.isfile(nombre_base_datos): # Validar si la base de datos existe

        print("Formato sugerido Fecha yyyy-MM-dd")
        FechaInicial = input("Ingrese fecha Inicial al Rango de Consulta: ").strip()
        fecha_inicio = FechaInicial.replace(" ","")+' 00:00'


        FechaFinal = input("Ingrese fecha Final al Rango de Consulta: ").strip()
        fecha_fin = FechaFinal.replace(" ","")+' 23:59'

        try:     # Conectar a la base de datos SQLite
            conexion = sqlite3.connect(nombre_base_datos, check_same_thread=False)
            cursor = conexion.cursor()

            # Consulta SQL para extraer los datos
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
                WHERE Created BETWEEN '{fecha_inicio}' AND '{fecha_fin}'
            """

            # Leer el contenido de out.txt
            with open(archivo_out_txt, "r") as archivo_out:
                numeros_documento_out = set(line.strip() for line in archivo_out)


            # Ejecutar la consulta SQL
            cursor.execute(consulta_sql)

            # Obtener los nombres de las columnas
            columnas = [descripcion[0] for descripcion in cursor.description]

            # Inicializar una lista para almacenar los JSON
            json_resultados = []

            # Iterar a través de los resultados
            for fila in cursor.fetchall():
                resultado = {
                    "id": fila[0],
                    "codigoEds": fila[1],
                    "codigoArticulo": fila[2],
                    "Cara": fila[3],
                    "codigoPosicion": fila[4],
                    "totalSurtidor": fila[5],
                    "volumen": fila[6],
                    "precio": fila[7],
                    "ROM": fila[8],
                    "placa": fila[9],
                    "tramaID": fila[10],
                    "Estado": 3,  # Valor predeterminado "Estado" como 3
                    "sectorVenta": fila[12],
                    "identificacionVendedor": fila[13],
                    "NumeroDocumento": fila[14],
                    "tipoVenta": fila[15],
                    "idTurno": fila[16],
                    "idVentaTI": fila[17],
                    "lecturaInicial": fila[18],
                    "lecturaFinal": fila[19],
                    "wId": fila[20],
                    "km": fila[21],
                    "nombreCliente": fila[22],
                    "fInicial": fila[23],
                    "fFin": fila[24]
                }
                # Verificar si el número de documento no está en out.txt
                numero_documento = resultado["NumeroDocumento"]
                if numero_documento not in numeros_documento_out:
                    json_resultados.append(resultado)

            # Crear la carpeta Json si no existe
            if not os.path.exists(carpeta_json):
                os.makedirs(carpeta_json)

            # Eliminar archivos JSON existentes en la carpeta
            for archivo_existente in os.listdir(carpeta_json):
                archivo_completo = os.path.join(carpeta_json, archivo_existente)
                if os.path.isfile(archivo_completo):
                    os.remove(archivo_completo)

            # Dividir los JSON en lotes de máximo 40 elementos
            max_elementos_por_lote = 40
            lotes_json = [json_resultados[i:i+max_elementos_por_lote] for i in range(0, len(json_resultados), max_elementos_por_lote)]
            
            # Guardar los JSON en archivos separados por lote
            for i, lote in enumerate(tqdm(lotes_json, desc="Creando lotes")):
                time.sleep(0.1)
                nombre_archivo_lote = os.path.join(carpeta_json, f"Lote_{i + 1}.json")
                with open(nombre_archivo_lote, "w") as archivo_json_lote:
                    json.dump(lote, archivo_json_lote, indent=2)

            print("Lotes de JSON creados y guardados en la carpeta 'Json'")

                # Verificar si el archivo output.txt existe y contiene datos obsoletos
            if os.path.exists("output.txt"):
                with open("output.txt", "r") as archivo_output:
                    numeros_documento_output = set(line.strip() for line in archivo_output)
            else:
                numeros_documento_output = set()

            # Encontrar los números de documento que no están en output.txt
            numeros_documento_nuevos = set(resultado["NumeroDocumento"] for resultado in json_resultados)
            numeros_documento_faltantes = numeros_documento_nuevos - numeros_documento_output

            # Limpiar y guardar números de documento en output.txt
            with open(archivo_output_txt, "w") as archivo_output:
                for resultado in json_resultados:
                    numero_documento = resultado["NumeroDocumento"]
                    archivo_output.write(numero_documento + "\n")


            print("Números de documento actualizados en 'output.txt'")
            time.sleep(0.3)

        except sqlite3.Error as error:
            print("Error al conectar a la base de datos SQLite:", error)
            time.sleep(0.3)
        finally:
            if conexion:
                conexion.close()
    else:
        print("La base de datos no existe.")
        time.sleep(0.3)



