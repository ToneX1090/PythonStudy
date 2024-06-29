class Player(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Team(object):

    def __init__(self,nome):
        self.teamname = nome
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)
    
    def print_players(self):
        print(f"Jogadores do {self.teamname}:")
        for player in self.players:
            print(player.name)

team = Team("Coringão")

team.add_player(Player("Cassio", 34))
team.add_player(Player("Gamarra", 53))
team.add_player(Player("Chicão", 43))
team.add_player(Player("José Maria", 75))
team.add_player(Player("Roberto Carlos", 51))
team.add_player(Player("Freddy Rincon", 50))
team.add_player(Player("Sócrates", 58))
team.add_player(Player("Marcelo Pereira", 52))
team.add_player(Player("CRAQUE Neto", 57))
team.add_player(Player("Ronaldo", 47))
team.add_player(Player("Carlitos Tevez", 40))

team.print_players()



