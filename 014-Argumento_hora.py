from datetime import datetime

atividade = input ("Digite a atividade feita: \n")
now = datetime.now()

f = open ("log.txt" , "a+")

data = now.strftime("%d/%m/%Y %H:%M:%S")
f.write(data + " " + atividade + "\n")

f.close()