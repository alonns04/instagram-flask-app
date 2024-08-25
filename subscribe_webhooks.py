import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
ig_id = os.getenv('IG_ID')
access_token = os.getenv('ACCESS_TOKEN')

# Definir la URL y parámetros
url = f"https://graph.instagram.com/v20.0/{ig_id}/subscribed_apps"
params = {
    'subscribed_fields': 'comments,messages,live_comments,message_reactions,messaging_optins,messaging_postbacks,messaging_referral,messaging_seen',
    'access_token': access_token
}

# Realizar la solicitud POST
response = requests.post(url, params=params)

# Mostrar el código de estado y el contenido de la respuesta
print(f"URL: {response.url}")
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")
