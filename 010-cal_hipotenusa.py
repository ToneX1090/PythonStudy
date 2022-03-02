import math
def hipotenusa(cata,cato):

    hipt1 = float (cato ** 2) + (cata ** 2)
    hipt2 = math.sqrt(hipt1)

    return hipt2

cato = float (input ("Digite o valor do cateto oposto: "))
cata = float (input ("Digite o valor do cateto adjacente: "))

hipotenusaT = hipotenusa(cata,cato)

print (f"O valor da hipotenusa é: {hipotenusaT:.2f}")