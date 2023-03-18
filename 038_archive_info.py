import sys
import os

archive = open(sys.argv[1], "r", encoding='utf-8')

size = os.path.getsize(archive)

print(size)

# "C:\Users\Milton\Documents\chorris.txt"