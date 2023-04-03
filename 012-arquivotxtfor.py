nome = input ("Digite o nome do arquivo: \n")
vezes = int (input ("Digite o numero de vezes vossa senhoria deseja imprimir o nome no arquivo: "))

f = open (f"{nome}.txt" , "a+")

for i in range(vezes):

    f.write(nome + "\n")

    print(nome)

f.close()
