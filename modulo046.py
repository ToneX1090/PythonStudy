def function_accuracy(jogador):

    jogador["taxa_de_conversão"] = (jogador["penalties_convertidos"] / jogador["penalties_cobrados"]) * 100

    print(f'O Jogador: {jogador["nome"]} tem uma taxa de conversão de: {jogador["taxa_de_conversão"]:.2f}%')