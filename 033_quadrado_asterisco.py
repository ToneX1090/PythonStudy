print("Vamos fazer um quadrado de asteriscos(*)")
colunas = int(input("digite o numero de colunas: "))
linhas = int(input("digite o numero de linhas: "))
ast = ""

for i in range(colunas):

    ast += "*"


print(" ")

for i in range(linhas):
    
    print(ast)
