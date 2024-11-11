# Holiday API - Python Function

Este proyecto contiene una función escrita en Python que utiliza la API de Calendarific para obtener los días festivos de un país en un año o mes específico. En este caso, se muestra cómo obtener los días festivos de Colombia para el año 2024.

## Descripción
La función `lambda_handler` realiza una solicitud a la API de Calendarific y devuelve una lista de días festivos para un año específico. La función está diseñada para ser utilizada en AWS Lambda o cualquier otro entorno que soporte Python y solicitudes HTTP.

La función permite obtener la siguiente información para cada día festivo:

- **Nombre del festivo**
- **Fecha del festivo**

## Requisitos
Antes de ejecutar este script, debes instalar las siguientes dependencias:

- `requests`: Para realizar las solicitudes HTTP.

```bash
pip install requests


Uso
la función está definida de la siguiente manera:


import requests
import json

def lambda_handler(event, context):
    # Definimos la URL y la clave de API
    url = "https://calendarific.com/api/v2/holidays"
    api_key = "tu_clave_api_aqui"

    # Definimos los parámetros de la solicitud
    params = {
        "api_key": api_key,
        "country": "CO",  # Colombia
        "year": "2024"    # Año 2024
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


## Parámetros de la Solicitud
La solicitud a la API de Calendarific requiere los siguientes parámetros:

| Parámetro | Descripción                                                    | Ejemplo                       |
|-----------|----------------------------------------------------------------|-------------------------------|
| api_key   | La clave de API que te proporciona Calendarific                | `lfAo5NQGAOYYKpNn5fYDvegMSGaNJChO` |
| country   | El código del país para el que quieres obtener los festivos.   | `CO` (Colombia)               |
| year      | El año para el que quieres obtener los festivos.               | `2024`                        |
| month     | *(Opcional)* El mes para el que quieres obtener los festivos.  | `12` (Diciembre)              |


## Respuesta de la API
La API devuelve un JSON con la siguiente estructura:

```json
{
    "response": {
        "holidays": [
            {
                "name": "Año Nuevo",
                "date": {
                    "iso": "2024-01-01"
                }
            },
            {
                "name": "Día de los Reyes Magos",
                "date": {
                    "iso": "2024-01-06"
                }
            },
            ...
        ]
    }
}



markdown
Copiar código
# Holiday API - Python Function

Este proyecto contiene una función escrita en Python que utiliza la API de Calendarific para obtener los días festivos de un país en un año o mes específico. En este caso, se muestra cómo obtener los días festivos de Colombia para el año 2024.

## Descripción
La función `lambda_handler` realiza una solicitud a la API de Calendarific y devuelve una lista de días festivos para un año específico. La función está diseñada para ser utilizada en AWS Lambda o cualquier otro entorno que soporte Python y solicitudes HTTP.

La función permite obtener la siguiente información para cada día festivo:

- **Nombre del festivo**
- **Fecha del festivo**

## Requisitos
Antes de ejecutar este script, debes instalar las siguientes dependencias:

- `requests`: Para realizar las solicitudes HTTP.

```bash
pip install requests
Uso
La función está definida de la siguiente manera:

python
Copiar código
import requests
import json

def lambda_handler(event, context):
    # Definimos la URL y la clave de API
    url = "https://calendarific.com/api/v2/holidays"
    api_key = "tu_clave_api_aqui"

    # Definimos los parámetros de la solicitud
    params = {
        "api_key": api_key,
        "country": "CO",  # Colombia
        "year": "2024"    # Año 2024
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
Parámetros de la Solicitud
La solicitud a la API de Calendarific requiere los siguientes parámetros:

Parámetro	Descripción	Ejemplo
api_key	La clave de API que te proporciona Calendarific	lfAo5NQGAOYYKpNn5fYDvegMSGaNJChO
country	El código del país para el que quieres obtener los festivos.	CO (Colombia)
year	El año para el que quieres obtener los festivos.	2024
month	(Opcional) El mes para el que quieres obtener los festivos.	12 (Diciembre)
Respuesta de la API
La API devuelve un JSON con la siguiente estructura:

json
Copiar código
{
    "response": {
        "holidays": [
            {
                "name": "Año Nuevo",
                "date": {
                    "iso": "2024-01-01"
                }
            },
            {
                "name": "Día de los Reyes Magos",
                "date": {
                    "iso": "2024-01-06"
                }
            },
            ...
        ]
    }
}
Ejemplo de Respuesta
Si se solicita la información de los días festivos para Colombia en el año 2024, la respuesta será una lista de diccionarios que contiene el nombre y la fecha de cada festivo:

json
Copiar código
[
    {
        "nombre": "Año Nuevo",
        "fecha": "2024-01-01"
    },
    {
        "nombre": "Día de los Reyes Magos",
        "fecha": "2024-01-06"
    },
    {
        "nombre": "Día de San José",
        "fecha": "2024-03-19"
    },
    ...
]
Función de Lambda
Este código está preparado para ser usado en un entorno como AWS Lambda. La función lambda_handler es la que será ejecutada cuando se reciba un evento. La respuesta se devuelve en formato JSON con el código de estado 200 y la lista de días festivos.

Notas
Asegúrate de reemplazar la clave de API por la tuya propia antes de ejecutar el código.
Si deseas obtener los festivos de un mes específico, puedes agregar el parámetro month en la solicitud.