import requests
import json

def lambda_handler(event, context):
    # Definimos la URL y la clave de API
    url = "https://calendarific.com/api/v2/holidays"
    api_key = "lfAo5NQGAOYYKpNn5fYDvegMSGaNJChO"

    # Definimos los parámetros de la solicitud
    params = {
        "api_key": api_key,
        "country": "CO",  # Colombia
        "year": "2024"    # Año 2024 (corregido)
    }

    # Hacemos la solicitud a la API
    response = requests.get(url, params=params)
    data = response.json()  # Extraemos el JSON de la respuesta

    # Filtrar y extraer la información de los días festivos
    holidays = data["response"]["holidays"]
    festivos = [
        {
            "nombre": holiday["name"],
            "fecha": holiday["date"]["iso"]
        } for holiday in holidays
    ]

    # Retornamos la respuesta en formato JSON
    return {
        'statusCode': 200,
        'body': json.dumps(festivos, ensure_ascii=False)
    }