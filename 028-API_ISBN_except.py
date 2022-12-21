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
       
        database = requests.get("https://openlibrary.org/isbn/"+realline+".json")
        json = database.json()
    
        newarchive.write("\nTitulo: " +json["title"])

newarchive.close()


#ISBN = sys.argv[1]
#database = requests.get("https://openlibrary.org/isbn/"+ISBN+".json")
#json = database.json()

#print("O livro buscado foi: " ,json["title"])
#print("A editora é: " ,json["publishers"])

#for linha in linhas:
    #try:
        #numero = int(linha)
    #except:
        #print (linha + "não é um numero")
        #exit()

    #sum_linha = sum_linha + numero

#avg_linha = sum_linha / len(linhas)

#print (avg_linha)


#8476696531
#978-8533613379

#C:\Users\Milton\Documents\ISBN.txt
