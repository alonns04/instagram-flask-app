from flask import Flask, request
import os
import requests

app = Flask(__name__)

def subscribe_webhooks():
    IG_ID = os.getenv('IG_ID')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    WEBHOOK_URL = 'https://instagram-flask-app.onrender.com/webhook'

    response = requests.post(
        f'https://graph.instagram.com/v20.0/{IG_ID}/subscribed_apps',
        params={
            'subscribed_fields': 'comments,messages',
            'access_token': ACCESS_TOKEN
        }
    )

    if response.status_code == 200:
        print('Suscripción exitosa:', response.json())
    else:
        print('Error en la suscripción:', response.status_code, response.text)

@app.before_first_request
def setup_webhooks():
    subscribe_webhooks()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)  # Imprime los datos recibidos en la consola para depuración
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
