import sys

#Definir fução
def conversao(temperatura):

    celcius = int((temperatura - 32)*5)/9
    return celcius



arquivo = open(sys.argv[1] , "r")
temperaturas = arquivo.readlines()

#Fazer a conversão // cria o txt "Celcius"

newarchive = open("Celsius.txt" , "a")

for temperatura in temperaturas:

    temperatura = float(temperatura)

    celcius = conversao(temperatura)

    newarchive.write(str(celcius) + " ")

newarchive.close()



#"C:\Users\Milton\Downloads\fahrenheit.txt"