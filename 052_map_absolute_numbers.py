input_list= input("Digite uma lista de numeros negativos: ")
user_list = input_list.split()

int_numbers = map (int, user_list)
negative_list = list(int_numbers)

absolute_numbers = map(abs, negative_list)

absolute_list = list(absolute_numbers)

print(f"A lista dada foi: {negative_list}")
print(f"A lista absoluta é: {absolute_list}")