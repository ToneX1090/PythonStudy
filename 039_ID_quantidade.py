

vendedores = dict()
id_vendedor = input("Qual o ID do vendedor? ")

while id_vendedor != "fim":

    quantidade = int(input("Qual a quantidade? "))

    if id_vendedor in vendedores:
        vendedores[id_vendedor] += quantidade
    else:
        vendedores[id_vendedor] = quantidade

    id_vendedor = input("Qual o ID do vendedor? ")

for vendedor in vendedores:
    print(f"O vendedor {vendedor} vendeu {vendedores.values(id_vendedor)} produtos.") 
