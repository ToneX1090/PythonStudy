import sys

#Definir fução
def conversao(temperatura):

    celcius = int((temperatura - 32)*5)/9
    return celcius



arquivo = open(sys.argv[1] , "r")
temperaturas = arquivo.readlines()

#Fazer a conversão

for temperatura in temperaturas:

    temperatura = float(temperatura)

    farh = conversao(temperatura)

    print(farh)





#"C:\Users\Milton\Downloads\fahrenheit.txt"