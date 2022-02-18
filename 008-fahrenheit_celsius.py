grausf = int (input ("Informe a temperatura Fahrenheit que deseja converter a Celsius: "))

grausc = int ((grausf - 32) * 5 ) / 9 

print (grausf , "°F é igual a " , "{:.1f}" .format(grausc) , "°C")

