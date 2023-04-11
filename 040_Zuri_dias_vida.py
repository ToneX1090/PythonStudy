from datetime import datetime
import sys
import json


archive = open(sys.argv[1], "r", encoding='utf-8')
json_txt = archive.read()

real_json = json.loads(json_txt)


now = datetime.now()
data_atual = now.strftime("%d/%m/%Y")
data_nascimento = real_json["nascimento"]
nome = real_json["nome"]

BD = datetime.strptime(data_nascimento, "%d/%m/%Y")
AD = datetime.strptime(data_atual, "%d/%m/%Y")

delta = AD - BD

print (f"\n {nome} tem {delta.days} dias!")







#"C:\Users\Milton\Documents\zuri_json.txt"