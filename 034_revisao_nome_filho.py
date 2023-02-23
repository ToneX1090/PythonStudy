name_mom = input("Digite o nome completo da mãe: ")
name_dad = input("Digite o nome completo do pai: ")
name_son = input("Digite o primeiro nome do filho(a): ")

list_name_dad = name_dad.split()
list_name_mom = name_mom.split()

print("O nome sugerido para seu filho(a) é: " + name_son + " " + list_name_dad[-1] + " " + list_name_mom[-1])