import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Usa la variable de entorno para el token de acceso
INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')

@app.route('/')
def hello_world():
    return '¡Hola, Mundo!'

@app.route('/instagram/media')
def get_instagram_media():
    url = f"https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,thumbnail_url,permalink&access_token={INSTAGRAM_ACCESS_TOKEN}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Error al obtener los datos"}), response.status_code
