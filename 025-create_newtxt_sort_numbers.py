import sys

archive=open(sys.argv[1], "r")
int_numbers = []
numbers = archive.readlines()

newarchive = open("sortednumbers.txt" , "w")

for number in numbers:

    realnumber = int(number.strip())

    int_numbers.append(realnumber)

sorted_numbers = sorted(int_numbers)    

for number in sorted_numbers:

    newarchive.write(f'{str(number)}\n')

newarchive.close()



# C:\Users\Milton\Documents\numbers.txt