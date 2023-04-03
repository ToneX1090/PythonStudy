import sys
import os
import os.path, time

archive = sys.argv[1]

split = archive.split("\\")
nome_txt = split[-1]
nome_arquivo = nome_txt.split(".")
nome = nome_arquivo[0]

caminho = os.path.dirname(os.path.abspath(archive))


tamanho_arquivo = os.stat(archive)
data_arquivo = os.path.getmtime(archive)
criacao_arquivo = os.path.getctime(archive)

new_archive = open (f"{caminho}\{nome}-info.txt" , "w")

new_archive.write(f"O tamanho do arquivo é: {tamanho_arquivo.st_size} bytes\n")
new_archive.write(f"A criação do arquivo foi em: {time.ctime(criacao_arquivo)}\n")
new_archive.write(f"A ultima modificação do arquivo foi em: {time.ctime(data_arquivo)}")


new_archive.close()


# Teste > "C:\Users\Milton\Documents\chorris.txt"
