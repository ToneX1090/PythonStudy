import sys
import requests

arquivo = open(sys.argv[1] , "r")
ISBN = arquivo.readlines()


newarchive = open("IBSN_TITLE.txt" , "a")

for linha in ISBN:

    realline = linha.strip()
    database = requests.get("https://openlibrary.org/isbn/"+realline+".json")
    json = database.json()

    
newarchive.write("Titulo: " ,json["title"])

newarchive.close()


#ISBN = sys.argv[1]
#database = requests.get("https://openlibrary.org/isbn/"+ISBN+".json")
#json = database.json()

#print("O livro buscado foi: " ,json["title"])
#print("A editora é: " ,json["publishers"])


#C:\Users\Milton\Documents\ISBN.txt