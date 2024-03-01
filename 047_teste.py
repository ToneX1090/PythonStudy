import sys
import requests

archive=open(sys.argv[1], "r")
books = archive.readlines()

newarchive = open("Booktitles.txt" , "w")
    
for book in books:

    realbook = book.strip()
    
    database = requests.get("https://openlibrary.org/isbn/"+ realbook+".json")
    json = database.json()
   
    title = json["title"]
    
    
    newarchive.write("\nTitulo: " +title)
    
    
newarchive.close()


#"C:\Users\Milton\Documents\047_livros.txt"