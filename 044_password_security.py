import re

password = input("Digite uma contrasenha forte que com mais de 8 caracteres: ")

if len(password) < 8:
    print("A senha informada tem menos de 8 caracteres, por favor, tente novamente!")
elif not any(c.isupper() for c in password):
    print("Para aumentar o nível da senha, coloque uma letra maiúscula.")
elif not any(c.islower() for c in password):
    print("Para aumentar o nível da senha, coloque uma letra minúscula.")
elif not re.search(r'[#!@%&$]', password):
    print("Para aumentar o nível da senha, coloque um caractere especial.")
elif not any(c.isdigit() for c in password):
    print("Para aumentar o nível da senha, coloque um número.")
else:
    print("Nivel de contrasenha forte.")