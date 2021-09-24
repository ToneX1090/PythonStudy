segundos_input = float (input ("Digite o número em segundos que deseja calcular: "))

horas = segundos_input // 3600
minutos = (segundos_input % 3600) // 60
segundos = segundos_input % (minutos * 60)


print(str(horas) + " horas")
print(str(minutos) + " minutos")
print(str(segundos) + " segundos")