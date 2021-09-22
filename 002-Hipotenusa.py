import math

oposto = float (input ("Digite o valor do cateto oposto: "))
adjacente = float (input ("Digite o valor do cateto adjacente: "))

hipotenusa = (oposto ** 2) + (adjacente ** 2)
hipotenusa2 = math.sqrt(hipotenusa)

print (f"O valor da Hipotenusa é : {hipotenusa2:.2f}")