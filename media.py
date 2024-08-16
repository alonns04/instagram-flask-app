import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
ig_id = os.getenv('IG_ID')
access_token = os.getenv('ACCESS_TOKEN')

# Definir la URL base
base_url = "https://graph.instagram.com/v20.0"

def make_request(url, params):
    """ Realiza una solicitud GET y devuelve la respuesta en formato JSON. """
    response = requests.get(url, params=params)
    
    # Mostrar la URL completa para depuración
    print(f"Request URL: {response.url}")
    
    # Mostrar el código de estado y el contenido de la respuesta
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    # Intentar decodificar el JSON solo si la respuesta es válida
    try:
        response_json = response.json()
        return response_json
    except ValueError as e:
        print(f"Error al decodificar JSON: {e}")
        return None

def get_profile_media(ig_id, access_token):
    """ Obtiene el ID de la primera publicación del perfil. """
    url = f"{base_url}/{ig_id}/media"
    params = {
        'fields': 'id,caption',
        'access_token': access_token
    }
    response_data = make_request(url, params)
    if response_data and 'data' in response_data:
        if response_data['data']:
            return response_data['data'][0]['id']
        else:
            print("No se encontraron publicaciones.")
            return None
    return None

def get_comments(post_id, access_token):
    """ Obtiene los comentarios de una publicación. """
    url = f"{base_url}/{post_id}/comments"
    params = {
        'access_token': access_token
    }
    response_data = make_request(url, params)
    if response_data and 'data' in response_data:
        if response_data['data']:
            return response_data['data']
        else:
            print("No se encontraron comentarios.")
            return []
    return []

# Obtener el ID de la publicación del perfil
profile_id = os.getenv('IG_ID')
post_id = get_profile_media(profile_id, access_token)

if post_id:
    print(f"Post ID: {post_id}")

    # Obtener y mostrar los comentarios
    comments = get_comments(post_id, access_token)
    for comment in comments:
        print(f"Comment ID: {comment['id']}")
        print(f"Comment Text: {comment['text']}")
        print(f"Comment Created Time: {comment['timestamp']}")
else:
    print("No se pudo obtener el ID de la publicación.")
