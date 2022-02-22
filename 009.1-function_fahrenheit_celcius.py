def conversao(grausf):

    grausc = int ((grausf - 32) * 5 ) / 9 

    return grausc


grausf = int (input ("Informe a temperatura Fahrenheit que deseja converter a Celsius: "))

convc = conversao(grausf)

print (grausf , "°F é igual a " , "{:.1f}" .format(convc) , "°C")