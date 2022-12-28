lists = [[3,5,7,9],[4,5,2,6],[1,4,5,5]]
list_number = []

for list in lists:

    avg_list = sum(list) / len(list)
    
    for element in list:
        if element > avg_list:
            list_number.append(element)
    

    print(len(list_number), "numeros estão acima da média",avg_list)
    print(list_number)
    list_number = []