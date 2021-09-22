peso = float (input ("Digite seu peso em kg: "))
altura = float (input("Indique sua altura (use '.' ex: 1.88)"))

imc = float(peso/(altura ** 2))

print ("Seu IMC é: " "{:.1f}" .format(imc))