#Receba um <argumento> que é o caminho de um arquivo.txt que contém várias linhas
import sys

arquivo=open(sys.argv[1], "r")
sum_linha = 0
linhas = arquivo.readlines()

#imprimir a média das linhas
for linha in linhas:
    try:

        numero = int(linha)
    except:
        print (linha + "não é um numero")
        exit()

    sum_linha = sum_linha + numero

avg_linha = sum_linha / len(linhas)

print (avg_linha)