numero = int(input("Digite até qual numero deseja brincar: "))
contador = 1

while contador <= numero:
    if contador % 7 == 0 or "7" in str(contador):
        print ("PI")
    else:
        print(contador)
    contador = contador + 1