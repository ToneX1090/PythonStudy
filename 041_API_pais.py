import requests

pais = input("Informe o país que deseja pesquisar: ")

database = requests.get(f"https://restcountries.com/v3.1/name/{pais}?fullText=true")
json = database.json()

if type(json) == dict:

    print(f"{pais} não foi encontrado, lembre-se que o nome deve estar em inglês. EX: Brazil")

else:
    nome = json[0]["name"]
    continente = json[0]["continents"]
    linguas = list(json[0]["languages"].values())

    print ("Nome: " , nome["common"])
    print ("Continente: " , continente[0])
    print ("População: " , json[0]["population"])
    print ("Linguas: " , ", ".join(linguas))
