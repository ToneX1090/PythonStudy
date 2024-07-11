class Pirate(object):
    def __init__(self, name, reward, fruit):
        self.name = name
        self.reward = float(reward)
        self.fruit = fruit

class Fruit(object):
    def __init__(self,fruit_name, rarity, power_lv):
        self.fruit_name = fruit_name 
        self.rarity = rarity
        self.power_lv = int(power_lv)

class Battle(object):
    def battle (self, pirate1, pirate2):

        print(f"A batalha entre os piratas {pirate1.name} e {pirate2.name} irá começar!\n")

        pirate1_power = pirate1.reward

        print(f"O pirata {pirate1.name} possui uma recompensa de B$ {pirate1.reward:.0f}.\n")
        
        if pirate1.fruit != None:
            pirate1_power += pirate1.fruit.power_lv
            print(f"O pirata {pirate1.name} comeu a {pirate1.fruit.fruit_name}.\n")
        else:
            print(f"O pirata {pirate1.name} não comeu nenhuma Akuma no mi!\n")
        
        pirate2_power = pirate2.reward

        print(f"O pirata {pirate2.name} possui uma recompensa de B$ {pirate2.reward:.0f}.\n") 

        if pirate2.fruit != None:
            pirate2_power += pirate2.fruit.power_lv
            print(f"O pirata {pirate2.name} comeu a {pirate2.fruit.fruit_name}.\n")
        else:
            print(f"O pirata {pirate1.name} não comeu nenhuma Akuma no mi!\n")

        if pirate1_power > pirate2_power:
            print(f"O pirata {pirate1.name} ganhou a batalha!")
        else:
            print(f"O pirata {pirate2.name} ganhou a batalha!")


#fruits
fruit_1 = Fruit("Hito Hito no mi", "rare", 4000)
fruit_2 = Fruit("Ope Ope no mi", "rare", 3000)
fruit_3 = Fruit("Abe Abe no mi", "uncommon", 2500)
fruit_4 = Fruit("Jiki Jiki no mi", "uncommon", 3000)
fruit_5 = Fruit("Wara Wara no mi", "uncommon", 2000)
fruit_6 = Fruit("Ryu Ryu no mi", "rare", 2000)
fruit_7 = Fruit("Oto Oto no mi", "common", 2000)
fruit_8 = Fruit("Smile", "common", 2500)
fruit_9 = Fruit("Toshi Toshi no mi", "rare", 2000)
fruit_10 = Fruit("Shiro Shiro no mi", "common", 2000)

#pirates
luffy = Pirate("Monkey D. Luffy", 3300000000, fruit_1)
law = Pirate("Trafalgar D. Law", 3000000000, fruit_2)
urogue = Pirate("Monge Uroge", 108000000, fruit_3)
kid = Pirate("Eustass Kid", 3000000000,fruit_4)
hawkins = Pirate("Basil Hawkins", 320000000, fruit_5)
drake = Pirate("X Drake", 222000000, fruit_6)
apoo = Pirate("Scratchmen Apoo", 350000000, fruit_7)
killer = Pirate("Killer", 162000000, fruit_8)
bonney = Pirate("Jewelry Bonney", 140000000, fruit_9)
bege = Pirate("Capone Gang Bege", 138000000, fruit_10)
zoro  = Pirate("Roronoa Zoro", 1111000000, None)

Battle().battle(luffy,law)
print("\n")
Battle().battle(zoro,killer)
print("\n")
Battle().battle(apoo,urogue)