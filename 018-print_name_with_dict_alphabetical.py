import sys

namelist = open(sys.argv[1] , "r" , encoding='utf-8')

cont = dict()

for name in namelist:

        realname = name.strip()
        firstname = realname.split()[0]
        #secondname = realname.split()[1]

        if firstname in cont:
            cont[firstname] +=1
        else:
            cont[firstname] = 1

for par in sorted (cont.items()):
    
    print(par)

    #"C:\Users\Milton\Downloads\nomes_com_sobrenome.txt"