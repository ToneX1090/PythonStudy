times = ["Flamengo", "Botafogo", "Palmeiras", "Fortaleza", "Cruzeiro", "São Paulo", "Bahia", "Athletico-PR", "Atlético-MG",
          "Bragantino", "Vasco", "Criciúma", "Juventude", "Internacional", "Corinthians", "Grêmio", "Vitória", "Cuiabá", "Fluminense",
        "Atlético-GO"]




for i in range(len(times)):
    for j in range(i + 1, len(times)):
        team1 = times[i]
        team2 = times[j]

    print(f"{team2} x {team1}")
    




# for casa in range(len(times)):   
      
#     time1 = times[casa]

#     for visita in times:

#         time2 = times[visita + 1]
    
#         print(f"{time1} x {time2}")