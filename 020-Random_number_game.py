import random

def game():

    random_number = random.randint(1,100)

    kick_number = int(input("Chute um numero entre 1 e 100: "))

    while random_number != kick_number:

        if random_number < kick_number:

            new_kick= int (input ("Tente um numero mais baixo: "))

        elif random_number > kick_number:
            
            new_kick= int (input ("Tente um numero mais alto: "))
        
        kick_number = new_kick

    else:
        print("Acertou 'Miseraví' !")


game()