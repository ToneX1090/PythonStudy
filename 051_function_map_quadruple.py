def quadruple(x):
    return x * 4

numbers = (input("Insira a lista que deseja quadriplicar: "))
real_numbers = numbers.split()

int_numbers = map (int, real_numbers)
int_list = list(int_numbers)


result = map(quadruple, int_list)
quadruple_list = list(result)

print(f"A lista quadruplicada é: {quadruple_list}")