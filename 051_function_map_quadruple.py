def quadruple(x):
    return x * 4

numbers = [1,2,3,4,10]

# real_numbers = numbers****
# int_numbers = list(map(int, real_numbers))


result = map(quadruple, numbers)
quadruple_list = list(result)

print(f"A lista quadruplicada é: {quadruple_list}")

#Try interact a input