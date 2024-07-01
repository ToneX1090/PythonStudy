class Pirate(object):
    def __init__(self, nome, recompensa, nome_fruta):
        self.nome = nome
        self.recompensa = float(recompensa)
        self.nome_fruta = nome_fruta

class Frute(object):
    def __init__(self,common,uncommon,rare,power_lv):
        self.common = common
        self.uncommon = uncommon
        self.rare = rare
        self.power_lv = int(power_lv)

class Battle(object):
    def __init__(self):


#colocar os supernovas
luffy = Pirate("Monkey D. Luffy", 3300000000,"Hito Hito", "rare", 4000)
law = Pirate("Trafalgar D. Law", 3000000000, "Ope Ope", "rare", 3000)
urogue = Pirate("Monge Uroge", 108000000, "Abe Abe", "uncommon", 2500)
kid = Pirate("Eustass Kid", 3000000000,"Jiki Jiki", "uncommon", 3000)
hawkins = Pirate("Basil Hawkins", 320000000, "Wara Wara", "Uncommon", 2000)
drake = Pirate("X Drake", 222000000, "Ryu Ryu", "rare", 2000)
apoo = Pirate("Scratchmen Apoo", 350000000, "Oto Oto", "common",2000 )
killer = Pirate("Killer", 162000000, "smile", "common", 2500)
bonney = Pirate("Jewelry Bonney", 140000000, "Toshi Toshi", "rare", 2000)
bege = Pirate("Capone Gang Bege", 138000000, "Shiro Shiro", "common", 2000)
zoro  = Pirate("Roronoa Zoro", 1111000000, False, False, 2600)



 