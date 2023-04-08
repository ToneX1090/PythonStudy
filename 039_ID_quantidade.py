

vendedores = dict()
id_vendedor = input("Qual o ID do vendedor? ")

while id_vendedor != "fim":

    quantidade = int(input("Qual a quantidade? "))

    if id_vendedor in vendedores:
        vendedores[id_vendedor] += quantidade
    else:
        vendedores[id_vendedor] = quantidade

    id_vendedor = input("Qual o ID do vendedor? ")
# se não colocar o .items() não é possivel iterar com k,v
for k, v in vendedores.items():
    print(f"O vendedor {k} vendeu {v} produtos.") 
