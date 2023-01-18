from datetime import datetime
import requests


now = datetime.now()
data = now.strftime("%d/%m/%Y %H:%M:%S")

def search_dollar():
    database = requests.get("https://api.hgbrasil.com/finance?key=45550550")
    json = database.json()

    cotacao = json["results"]["currencies"]["USD"]

    print(data)
    print("A valor atual do dollar é : R$",cotacao["sell"])