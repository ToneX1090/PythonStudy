lists = [[3,5,7,9],[4,5,2,6],[1,4,5,5]]
list_number = []
average_list = []

for list in lists:
    list_number += list

average = sum(list_number) / len(list_number)

for element in list_number:
    if element > average:
        average_list.append(element)

print(len(average_list), "numeros estão acima da média {:.1f} " .format(average))
print(average_list)