times = ["Flamengo", "Botafogo", "Palmeiras", "Fortaleza", "Cruzeiro", "São Paulo", "Bahia", "Athletico-PR", "Atlético-MG",
          "Bragantino", "Vasco", "Criciúma", "Juventude", "Internacional", "Corinthians", "Grêmio", "Vitória", "Cuiabá", "Fluminense",
        "Atlético-GO"]



while times >= range(2):

    for i in range(len(times)):
        for j in range(i + 1, len(times)):
            away = times[i]
            home = times[j]

        print(f"{home} x {away}")
    
    times.remove[j]
    




# for casa in range(len(times)):   
      
#     time1 = times[casa]

#     for visita in times:

#         time2 = times[visita + 1]
    
#         print(f"{time1} x {time2}")

############################################

# pseudocodigo aqui:

# simular_campeonato():
#     for rodada in range(self.num_rodadas):
#         simular_rodada()

# simular_rodada():
#     jogos = montar_jogos()

#     for jogo in jogos:
#         executar_jogo()

# montar_jogos():
#     # TODO: implementar