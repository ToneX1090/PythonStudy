import sys
import os
import os.path, time

arquivo = sys.argv[1]

tamanho_arquivo = os.stat(arquivo)
data_arquivo = os.path.getctime(arquivo)

print("O tamanho do arquivo é: " , tamanho_arquivo.st_size, "bytes")
print("A ultima modificação do arquivo foi em: " , time.ctime(data_arquivo))