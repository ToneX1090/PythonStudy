from datetime import datetime
import requests


now = datetime.now()
data = now.strftime("%d/%m/%Y %H:%M:%S")

database = requests.get("https://hgbrasil.com/status/finance")

print(now)
print(data)
print(database)