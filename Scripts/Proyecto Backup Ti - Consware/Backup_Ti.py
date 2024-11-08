import os
import re
import json


archivo_entrada = "LogTi.txt"
archivo_salida = "ResultadoTi.txt"
archivo_salidaFinVenta = "Resultado.txt"


if os.path.exists(archivo_salida):
    with open(archivo_salida, "w"):
        pass  

patron_preguntar_venta = r'trama recibida PreguntarVenta: (\d+)\s*\n\s*Trama leida de memoria SD:\s*({.*?})\s*'


json_unicos = []
json_unicos2 = []
SECVTM = set()


def agregar_json_unico(secVta, json_nuevo):

    if secVta not in SECVTM:
        json_unicos.append(json_nuevo)


def agregar_json_unico2(secVta, json_nuevo2):

    if secVta not in SECVTM:
        json_unicos2.append(json_nuevo2)



with open(archivo_entrada, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

    coincidencias = re.finditer(patron_preguntar_venta, contenido, re.DOTALL)

    for coincidencia in coincidencias:

        secVta = coincidencia.group(1)
        json_texto = coincidencia.group(2).strip()

        #if secVta not in SECVTM: 
            #SECVTM.add(secVta)


        # Limpiar el valor problemático y volver a intentar
        json_texto = json_texto.replace('', '')
        
        try:
            json_venta = json.loads(json_texto)
            
            agregar_json_unico(secVta, json_venta)

            json_venta_modificado = {
                "id": json_venta.get("id"),
                "codigoEds": json_venta.get("codEds"),
                "codigoArticulo": json_venta.get("codArt"),
                "Cara": json_venta.get("Cara"),
                "codigoPosicion": json_venta.get("codPos"),
                "totalSurtidor": json_venta.get("totSur"),
                "volumen": json_venta.get("vol"),
                "precio": json_venta.get("precio"),
                "ROM": json_venta.get("ROM"),
                "placa": json_venta.get("placa"),
                "tramaID": json_venta.get("trID"),
                "Estado": 3,
                "sectorVenta": json_venta.get("secVta"),
                "identificacionVendedor": json_venta.get("idVdor"),
                "NumeroDocumento": json_venta.get("NDoc"),
                "tipoVenta": json_venta.get("tVen"),
                "idTurno": json_venta.get("idTurno"),
                "idVentaTI": json_venta.get("idVentaTI"),
                "lecturaInicial": json_venta.get("lecIn"), 
                "lecturaFinal": json_venta.get("lecFin"),
                "wId": json_venta.get("wId"),
                "km": json_venta.get("km"),
                "nombreCliente": json_venta.get("nombreCliente"),
                "fInicial": "2023/11/27 10:21:21",
                "fFin": "2023/11/27 10:21:21"
            }

            agregar_json_unico2(secVta, json_venta_modificado)

            if secVta not in SECVTM: 
                SECVTM.add(secVta)

        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")

with open(archivo_salida, "w", encoding="utf-8") as archivo_salida:
    for json_unico in json_unicos:
        archivo_salida.write(json.dumps(json_unico, ensure_ascii=False))
        archivo_salida.write(",\n")  

with open(archivo_salidaFinVenta, "w", encoding="utf-8") as archivo_salidaFinVenta:
    for json_unico in json_unicos2:
        archivo_salidaFinVenta.write(json.dumps(json_unico, ensure_ascii=False))
        archivo_salidaFinVenta.write(",\n")         
