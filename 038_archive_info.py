import sys
import os
import os.path, time

archive = sys.argv[1]

tamanho_arquivo = os.stat(archive)
data_arquivo = os.path.getctime(archive)

print("O tamanho do arquivo é: " , tamanho_arquivo.st_size, "bytes")
print("A ultima modificação do arquivo foi em: " , time.ctime(data_arquivo))

# "C:\Users\Milton\Documents\chorris.txt"
#archive = sys.argv[1]
#archive = open(sys.argv[1], "r", encoding='utf-8')