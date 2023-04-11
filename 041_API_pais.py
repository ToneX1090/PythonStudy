import requests

pais = input("Informe o país que deseja pesquisar: ")
database = requests.get(f"https://restcountries.com/v3.1/name/{pais}?fullText=true")
json = database.json()

nome = json[0]["name"]
continente = json[0]["continents"]
linguas = json[0]["languages"]



print ("Nome: " , nome["common"])
print ("Continente: " , continente[0])
print ("População: " , json[0]["population"])
print ("Linguas: " , linguas)
