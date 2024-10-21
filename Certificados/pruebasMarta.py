import json
import csv

csv_file_path = 'certificates.csv'
json_file_path = 'api_simulada.json'

def leer_datos_csv(csv_file_path):
    datos = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            datos.append(row)
    return datos

def getCertificado(sys_id, file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            certificado = next((item for item in data if item["fingerprint"] == sys_id), None)
            if not certificado:
                raise Exception("Certificado no encontrado")
            return certificado
    except Exception as er:
        raise er

def putCertificado(sys_id, registro, file_path):
    try:
        with open(file_path, 'r+') as file:
            data = json.load(file)
            certificado = next((item for item in data if item["fingerprint"] == sys_id), None)
            if not certificado:
                raise Exception("Certificado no encontrado")
            
            # Actualizar el certificado con los datos del registro
            certificado.update(registro)
            
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            return certificado
    except Exception as er:
        raise er

def postCertificado(registro, file_path):
    try:
        with open(file_path, 'r+') as file:
            data = json.load(file)
            data.append(registro)
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            return registro
    except Exception as er:
        raise er

# Leer datos del archivo CSV
datos_csv = leer_datos_csv(csv_file_path)

# Procesar cada registro del CSV
for registro in datos_csv:
    try:
        # Intentar obtener el certificado
        certificado = getCertificado(registro['fingerprint'], json_file_path)
        print(f"Certificado encontrado: {certificado}")
        
        # Si se encuentra, hacer PUT para actualizarlo
        updated_certificado = putCertificado(
            registro['fingerprint'],
            registro,
            json_file_path
        )
        print(f"Certificado actualizado: {updated_certificado}")
    except Exception as e:
        # Si no se encuentra, hacer POST para crearlo
        new_certificado = postCertificado(
            registro,
            json_file_path
        )
        print(f"Nuevo certificado creado: {new_certificado}")