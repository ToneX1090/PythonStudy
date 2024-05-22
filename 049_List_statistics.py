list = [5,7,10,8,10,2,7,2,7]
sigma = 0

for number in list:

    sigma += number

average = sigma/len(list)
print(f"A média da lista é: {average}") #add decimals

cont = dict()

for number in list:
    
    if number in cont:        
        cont[number] += 1
    else:
        cont[number] = 1

#corrigir esta parte
mode = 0
value = 0 
for k,v in sorted (cont.items()):
               
        if mode == 0:
            mode = k
        elif value < v:
             mode = k
        value = v
        print(mode)
print(cont)
