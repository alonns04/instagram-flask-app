from flask import Flask, request, template_rendered
import os
import requests

app = Flask(__name__)

@app.route('/')
def home():
    template_rendered('../home/home.html')

if __name__ == '__main__':
    app.run(debug=True)
