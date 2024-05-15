import sys
import requests

def title_name(ISBN):
    try:
        database = requests.get("https://openlibrary.org/isbn/"+ISBN+".json")
        json = database.json()
    except:
        newarchive.write("\n" +ISBN+"  : Este ISBN não é valido.")
    else:
        title = json["title"]
        newarchive.write("\nTitulo: " +title)

archive=open(sys.argv[1], "r")
books = archive.readlines()

newarchive = open("Booktitles.txt" , "w")
    
for book in books:
    realbook = book.strip()
    title_name(realbook)
newarchive.close()


#"C:\Users\Milton\Documents\047_livros.txt"
#Necessário arrumar o try/except - inserir strip