segundos_input = float (input ("Digite o número que deseja calcular, em segundos: "))

horas = segundos_input // 3600
minutos = (segundos_input % 3600) // 60
segundos = (segundos_input % 3600 ) % 60


print(str(horas) + " horas")
print(str(minutos) + " minutos")
print(str(segundos) + " segundos")
