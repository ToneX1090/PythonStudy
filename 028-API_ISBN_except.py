import sys
import requests

arquivo = open(sys.argv[1] , "r")
ISBN = arquivo.readlines()


newarchive = open("IBSN_TITLE.txt" , "w")

for linha in ISBN:

    realline = linha.strip()

    if len(realline) != 14 and len(realline)!= 10:

        newarchive.write("\n" +realline+"  Este ISBN não é valido.") 

    else:
        #verificar se o json é valido
        try:
            database = requests.get("https://openlibrary.org/isbn/"+realline+".json")
            json_validation = database.json()
        except:
            newarchive.write("\n" +realline+"  : Este ISBN não é valido.")
        else:  
            newarchive.write("\nTitulo: " +json_validation["title"])

newarchive.close()


#C:\Users\Milton\Documents\ISBN.txt
