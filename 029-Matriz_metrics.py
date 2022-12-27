

lists = [[3,5,7,9],[4,5,2,6],[1,4,5]]
cont = 0
list_number = []

for list in lists:

    avg_list = sum(list) / len(list)
    
    if list[cont] > avg_list:

       del(list[cont])
       cont = cont + 1
    

    print(len(list), "numeros estão acima da média")
    print(list)

    #tentar com 2 for
    #
    ##
    # for element in list:
        #if element < avg_list:
        #del(list[element])