peso = float (input ("Digite seu peso em kg: "))
altura = float (input("Indique sua altura (use '.' ex: 1.88)"))

imc = float(peso/(altura ** 2))

if imc < 18.5:

    print ("Seu IMC é, {:.1f}" .format(imc) + " e está inferior ao normal")

elif imc >= 18.5 and imc <= 24.9:
    
    print ("Seu IMC é, {:.1f}" .format(imc) + " e é considerado normal")

elif imc >= 25.9 and imc <= 30:

    print ("Seu IMC é, {:.1f}" .format(imc) + " e é superior ao normal")

else:

    print ("Seu IMC é, {:.1f}" .format(imc) + " e é considerado obesidade, procure um nutricionista")
