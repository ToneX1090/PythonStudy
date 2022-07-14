import sys
import requests

cep = sys.argv[1]
v_link = requests.get("https://viacep.com.br/ws/"+cep+"/json/")
v_json = v_link.json()

if cep == v_json["cep"]:

    print ("\nRua: " , v_json["logradouro"])
    print ("Cidade: " , v_json["localidade"])
    print ("Bairro: " , v_json["bairro"])
    print ("Estado: " , v_json["uf"])

    #tratar argumento .format .strip