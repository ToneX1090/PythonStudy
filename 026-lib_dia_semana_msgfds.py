from datetime import date

#Como esta função date.today().weekday() devolve um numero de 0 à 6, é nevessário criar uma lista para pegar o nome por indice.
days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
#Indice----0----------1---------2--------3---------4---------5---------6-----

week_day = date.today().weekday()

#os finais de semana são os indices 5 e 6, por este motivo, tudo menor que isso é dia útil.
if week_day < 4:

    print(f"Hoje é dia útil, feliz {days[week_day]}-Feira")

elif week_day == 4:

    print("Sextoooooou meu patrão !")

else:
    
    print(f"Hoje é {days[week_day]}, aproveite seu fim de semana.")
