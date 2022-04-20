import sys

namelist = open(sys.argv[1] , "r")
cont = dict() 

for name in namelist:
     if name in cont:
         cont[name] += 1
       
     else:
         cont[name] = 1
     
print(cont)



# "C:\Users\Milton\Downloads\nomes.txt"