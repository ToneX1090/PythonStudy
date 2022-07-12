import sys
import json

arquivo = open(sys.argv[1], "r", encoding='utf-8')
json_txt = arquivo.read()

real_json = json.loads(json_txt)

print ("\nNome: " ,real_json["nome"])
print ("Idade: " ,real_json["idade"])


#"C:\Users\Milton\Downloads\pessoa.txt"