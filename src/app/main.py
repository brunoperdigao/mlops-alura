from typing import List
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob

import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



### Model Training

colunas_input = ['tamanho', 'ano', 'garagem']

input = open("../../models/modelo-salvo", "rb")
modelo = pickle.load(input)


### Flask API

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)

@app.route("/")
def home():
    return "Minha primeira API."

@app.route("/sentimento/<frase>")
@basic_auth.required
def sentimento(frase: str) -> float:
    tb = TextBlob(frase)
    tb_en = tb.translate(from_lang="pt_br", to="en")
    polaridade = tb_en.sentiment.polarity
    return f"A polaridade dessa frase é {polaridade:.2f}"

@app.route("/cotacao/", methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas_input]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
