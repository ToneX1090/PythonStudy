import sys
import json

arquivo = open(sys.argv[1], "r", encoding='utf-8')
json_txt = arquivo.read()

jogadores = json.loads(json_txt)
maior_taxa = {}

for jogador in jogadores:
    jogador["taxa_de_conversão"] = (jogador["penalties_convertidos"] / jogador["penalties_cobrados"]) * 100

    if len(maior_taxa) == 0:
        maior_taxa = jogador
    elif maior_taxa["taxa_de_conversão"] < jogador["taxa_de_conversão"]:
        maior_taxa = jogador

print("O jogador com maior taxa taxa de converção é: " ,maior_taxa["nome"])
print(f'Com uma taxa de: {maior_taxa["taxa_de_conversão"]:.2f}%')


#"C:\Users\Milton\Documents\penalty_json.txt"