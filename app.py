from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Instagram API Flask App"

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Aquí gestionas los datos del webhook de Instagram
    return jsonify({"status": "success"})
