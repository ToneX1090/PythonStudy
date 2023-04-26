class pirata(object):

    def __init__(self, nome, recompensa, fruta):
        self.nome = nome
        self.recompensa = recompensa
        self.fruta = fruta

    def imprimir_cartaz(self):
        print(f"O pirata {self.nome} tem uma recompensa de {self.recompensa}.")

    def pode_nadar(self):
        if self.fruta:
            print(f"O Pirata {self.nome} comeu a {self.fruta} No Mi e não pode nadar.")
        else:
            print(f"O pirata {self.nome} não comeu nenhuma Akuma no Mi e pode nadar tranquilo!")

luffy = pirata("Monkey D. Luffy","B$ 3.300.000.000","Gomu Gomu")
law = pirata("Trafalgar D. Law","B$ 3.000.000.000", "Ope Ope")
shanks = pirata("Shanks O Ruivo","B$ 4.048.900.000", False)


luffy.imprimir_cartaz()
luffy.pode_nadar()

law.imprimir_cartaz()
law.pode_nadar()

shanks.imprimir_cartaz()
shanks.pode_nadar()