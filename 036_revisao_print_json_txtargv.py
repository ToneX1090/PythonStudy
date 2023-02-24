import sys
import json

# encoding='utf-8' serve para aceitar acentos e ç
archive = open(sys.argv[1], "r", encoding='utf-8')
json_txt = archive.read()

real_json = json.loads(json_txt)

print ("\nNome: " ,real_json["nome"])
print ("Raça: " ,real_json["raça"])
print ("Idade: " ,real_json["idade"])

#"C:\Users\Milton\Documents\cachorro_json.txt"