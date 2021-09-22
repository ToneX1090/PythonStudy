entrada = float( input ("Informe o numero a ser informado: "))
contador = 0

while contador <= entrada:
    
    if contador % 2 == 0:
        print (f"O numero {contador:.0f} é par")
    else:
        print (f"O numero {contador:.0f} é impar")

    contador = contador + 1
