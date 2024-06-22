class Player(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Team(object):

    def __init__(self,nome, players):
        self.teamname = nome
        self.players = []
    
    def add_player(self):
        #develop
    
    def print_player(self):
        print(f"O jogador {self.name} tem {self.age} anos.")


Cassio = Player("Cassio", 34)
Gamarra = Player("Gamarra", 53)
Chicao = Player("Chicão", 43)
Ze_Maria = Player("José Maria", 75)
Roberto_Carlos = Player("Roberto Carlos", 51)
Rincon = Player("Freddy Rincon", 50)
Socrates = Player("Sócrates", 58)
Marcelinho = Player("Marcelo Pereira", 52)
Neto = Player("CRAQUE Neto", 57)
Fenomeno = Player("Ronaldo", 47)
Tevez = Player("Carlitos Tevez", 40)
