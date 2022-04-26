import sys

namelist = open(sys.argv[1] , "r")

cont = dict() 

for name in namelist:

    realname = name.strip()

    if realname in cont:
         
         cont[realname] += 1
       
    else:
         cont[realname] = 1
   
for par in cont.items():

    print(par)

# "C:\Users\Milton\Downloads\nomes.txt"