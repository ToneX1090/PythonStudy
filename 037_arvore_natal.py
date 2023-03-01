altura = int(input("Informe a altura da arvore: "))
inicio = altura - 1
fim = altura - 2
asterisco = 1
base = "***\n"


for i in range(altura):
    print( inicio * " "+ asterisco * "*")
    asterisco += 2
    inicio -= 1
print(2 * (fim * " " + base))