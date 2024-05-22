import random

random_number = random.randint(1,100)
cont = 1
first_kick = int(input("Chute um numero entre 1 e 100: "))

while random_number != first_kick:

    cont +=1

    if random_number < first_kick:
        new_kick= int(input ("Tente um numero mais baixo: "))
    elif random_number > first_kick:            
        new_kick= int(input ("Tente um numero mais alto: "))
        first_kick = new_kick
else:
    print(f"Acertou em {cont} tentativas, 'Miseraví'!")