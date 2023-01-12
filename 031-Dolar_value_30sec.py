from datetime import datetime
import requests


now = datetime.now()
data = now.strftime("%d/%m/%Y %H:%M:%S")

database = requests.get("https://api.hgbrasil.com/finance?key=45550550")
json = database.json()

print(now)
print(data)
print(json["USD"])