import datetime

day = datetime.date.today().day
year = datetime.date.today().year
month = datetime.date.today().month
week = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
day_week = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta")

#verifica se qual dia é hoje "padrão americano aaaa/mm/dd"
num = datetime.date(ano, mês, dia).weekday()
p = (sem[num])