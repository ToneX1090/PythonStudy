nome = input ("Digite o nome do arquivo: \n")
vezes = int (input ("Digite o numero de vezes vossa senhoria deseja imprimir o nome no airquivo: "))

f = open (f"{nome}.txt" , "w")

for i in range(vezes):

    f.write(nome + "\n")

f.close()
