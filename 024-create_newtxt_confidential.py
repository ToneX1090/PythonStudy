import sys
import re

first_txt=open(sys.argv[1], "r")

linhas = first_txt.readlines()

newarchive = open("confidential2.txt" , "w")

for linha in linhas:
    if not linha.startswith("Confidential:"):
    
        newtext = re.sub("\d","x", linha)

        newarchive.write(newtext)

newarchive.close()








# C:\Users\Milton\Documents\confidential.txt