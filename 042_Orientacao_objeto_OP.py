class pirata(object):

    def __init__(self, name, reward, fruit):
        self.name = name
        self.reward = reward
        self.fruit = fruit

    def print_poster(self):
        print(f"O pirata {self.name} tem uma recompensa de {self.reward}.")

    def can_swim(self):
        if self.fruit:
            print(f"O Pirata {self.name} comeu a {self.fruit} No Mi e não pode nadar.")
        else:
            print(f"O pirata {self.name} não comeu nenhuma Akuma no Mi e pode nadar tranquilo!")

luffy = pirata("Monkey D. Luffy","B$ 3.300.000.000","Gomu Gomu")
law = pirata("Trafalgar D. Law","B$ 3.000.000.000", "Ope Ope")
shanks = pirata("Shanks O Ruivo","B$ 4.048.900.000", False)


luffy.print_poster()
luffy.can_swim()

law.print_poster()
law.can_swim()

shanks.print_poster()
shanks.can_swim()