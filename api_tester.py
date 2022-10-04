import requests

params = {
        "tamanho": 120,
        "ano": 2001,
        "garagem": 2
        }
endpoint = 'http://127.0.0.1:5000/cotacao/'
response = requests.post(endpoint, json=params)
print(response.text)
