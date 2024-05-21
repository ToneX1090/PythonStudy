import sys
import requests

def title_name(ISBN):
    response = requests.get("https://openlibrary.org/isbn/"+ISBN+".json")
    if response.status_code != 200:
        error_text = "\n" +ISBN.strip()+" : Este ISBN não é valido."
        print(error_text)
        newarchive.write(error_text)
    else:
        json = response.json()
        title = json["title"]
        success_text = "\n" +ISBN.strip()+" : " +title
        print(success_text)
        newarchive.write(success_text)

archive=open(sys.argv[1], "r")
books = archive.readlines()

newarchive = open("Booktitles.txt" , "w")
    
for book in books:
    title_name(book)
newarchive.close()


#"C:\Users\Milton\Documents\047_livros.txt"