import sys
import requests

def title_name(ISBN):

    database = requests.get("https://openlibrary.org/isbn/"+ISBN+".json")
    json = database.json()

    title = json["title"]
    print(title)
    

    # full_title = json["full_title"]
    
    # return f"\nTitulo - {full_title}"
    
    # return json

archive=open(sys.argv[1], "r")
books = archive.readlines()

# newarchive = open("Booktitles.txt" , "w")
    
for book in books:
    #newarchive.write(title_name(book))
    title_name(book)
# newarchive.close()


#"C:\Users\Milton\Documents\047_livros.txt"