import sys

archive=open(sys.argv[1], "r")

numbers = archive.readlines()
int_numbers = []

for number in numbers:

    realnumber = int(number.strip())

    int_numbers.append(realnumber)

print(sorted(int_numbers))



# C:\Users\Milton\Documents\numbers.txt