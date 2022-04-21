import sys

namelist = open(sys.argv[1] , "r")

cont = dict() 

for name in namelist:

     if name.strip() in cont:
         
         cont[name.strip()] += 1
       
     else:
         cont[name.strip()] = 1
   
print(cont)

# "C:\Users\Milton\Downloads\nomes.txt"