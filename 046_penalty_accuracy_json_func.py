import sys
import json
import modulo046

arquivo = open(sys.argv[1], "r", encoding='utf-8')
json_txt = arquivo.read()

jogadores = json.loads(json_txt)

for jogador in jogadores:
   modulo046.function_accuracy(jogador)