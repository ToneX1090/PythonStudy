list = [5,7,8,10,2,7,2,6,10]
sigma = 0

#Average
for number in list:

    sigma += number

average = sigma/len(list)
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