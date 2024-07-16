class Team(object):
    def __init__(self, name, team_nv, points):
        self.name = name
        self.team_nv = team_nv
        self.points = points

class Championship(object):
    def __init__(self):
        self.table = []
    

    def first_round(self, team):
        self.table.append(team)

Team("Athletico", 6, 0)
Team("Atlético-GO",4, 0)
Team("Atlético-MG",8, 0)
Team("Bahia",6, 0)
Team("Botafogo",6 ,0)
Team("Bragantino",7, 0)
Team("Corinthians", 5, 0)
Team("Criciúma", 5, 0)
Team("Cruzeiro", 7, 0)
Team("Cuiabá", 4, 0)
Team("Flamengo", 8, 0)
Team("Fluminense", 3, 0)
Team("Fortaleza", 6, 0)
Team("Grêmio", 3, 0)
Team("Internacional", 4, 0)
Team("Juventude", 2, 0)
Team("Palmeiras", 8, 0)
Team("São Paulo", 6, 0)
Team("Vasco", 3, 0)
Team("Vitória", 3, 0)










#campeonato
#simular 38 rodadas 
#randomizar as partidas
#todos jogam contra todos
#não repetir jogos mais de 2x > começar apenas com primeira rodada

#possibilidades:
#empate +1
#vitoria +3
#derrota 0

#listar a tabela final