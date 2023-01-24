from datetime import datetime
import requests
import time

count = 20


def search_dollar():
    database = requests.get("https://api.hgbrasil.com/finance?key=45550550")
    json = database.json()

    cotacao = json["results"]["currencies"]["USD"]

   
    print("O valor atual do dollar é : R$ {:.2f}" .format(cotacao["sell"]))

while count != 0:
    
    now = datetime.now()
    data = now.strftime("%d/%m/%Y %H:%M:%S")
    
    print(data)
    search_dollar()
    time.sleep(30)
    count = count - 1


#mostrar 2 numeros após a vorgula
#melhorae vizualização da data