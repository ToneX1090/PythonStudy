nota1 = float (input ("Digite a nota do primeiro bimestre: "))
nota2 = float (input ("Digite a nota do segundo bimestre: "))
nota3 = float (input ("Digite a nota do terceiro bimestre: "))
nota4 = float (input ("Digite a nota do quarto bimestre: "))

media = float (nota1 + nota2 + nota3 + nota4) / 4

if media > 7:

    print ("Parabéns ! você foi aprovado. Sua média foi:{:.1f}" .format(media))

elif media <= 6.9 and media >= 5:

    print("Quase, você ficou de recuperação. Sua média foi:{:.1f}" .format(media))

else:

    print ("Que pena, você foi reprovado. Sua média foi:{:.1f}" .format(media))