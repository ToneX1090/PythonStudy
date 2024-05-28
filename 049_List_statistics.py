list = [5,7,8,10,2,7,2,6,10]
sum = 0

#Average
for number in list:

    sum += number

average = sum/len(list)
print(f"A média da lista é: {average:.2f}")

cont = dict()

for number in list:
    
    if number in cont:        
        cont[number] += 1
    else:
        cont[number] = 1

#Mode
mode = 0
value = 0 
for k,v in cont.items():
    if v > value:
        mode = k
        value = v
print(f"A moda é: {mode}")

#Median
sorted_list = sorted(list)
median = 0

if len(list)%2 == 0:
    left = sorted_list[len(list)//2]
    right = sorted_list[(len(list)//2)-1]

    median = (right+left)/2
else:
    median = sorted_list[len(list)//2]
print(f"A mediana é: {median}")

#Standard deviation

sum_sd = 0
for number in list:
    cont_sd = (number - average) **2
    
    sum_sd += cont_sd

standart_dev = (sum_sd/len(list)) ** 0.5

print(f"O desvio padrão é: {standart_dev:.2f}")
    