class Team(object):
    def __init__(self, name, team_nv, points):
        self.name = name
        self.team_nv = team_nv
        self.points = points

class Championship(object):
    def __init__(self):
        self.table = []

    def add_team(self, team):
        self.table.append(team)

    def first_round()
        #criar um laço que mantém fixo o primeiro time e o compara com todos os outros

        # Simular todos os jogos
            # for i in range(len(self.table)):
            #     for j in range(i + 1, len(self.table)):
            #         team1 = teams[i]
            #         team2 = teams[j]



        #somar o numero de pontos feitos em uma variavel points

        #if team1.team_lv == team2.team_lv:
        #   team1.points += 1
        #elif team1.team_lv > team2.team_lv:        
        #    team1.points += 3
        #else:
        #    team1.points += 0
        #         
        #repetir para todos os times


brazilian_championship = Championship()  

brazilian_championship.add_team(Team("Athletico-PA", 6, 0))
brazilian_championship.add_team(Team("Atlético-GO",4, 0))
brazilian_championship.add_team(Team("Atlético-MG",8, 0))
brazilian_championship.add_team(Team("Bahia",6, 0))
brazilian_championship.add_team(Team("Botafogo",6 ,0))
brazilian_championship.add_team(Team("Bragantino",7, 0))
brazilian_championship.add_team(Team("Corinthians", 5, 0))
brazilian_championship.add_team(Team("Criciúma", 5, 0))
brazilian_championship.add_team(Team("Cruzeiro", 7, 0))
brazilian_championship.add_team(Team("Cuiabá", 4, 0))
brazilian_championship.add_team(Team("Flamengo", 8, 0))
brazilian_championship.add_team(Team("Fluminense", 3, 0))
brazilian_championship.add_team(Team("Fortaleza", 6, 0))
brazilian_championship.add_team(Team("Grêmio", 3, 0))
brazilian_championship.add_team(Team("Internacional", 4, 0))
brazilian_championship.add_team(Team("Juventude", 2, 0))
brazilian_championship.add_team(Team("Palmeiras", 8, 0))
brazilian_championship.add_team(Team("São Paulo", 6, 0))
brazilian_championship.add_team(Team("Vasco", 3, 0))
brazilian_championship.add_team(Team("Vitória", 3, 0))

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