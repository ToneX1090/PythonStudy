import sys
import requests

ISBN = sys.argv[1]
database = requests.get("https://openlibrary.org/isbn/"+ISBN+".json")
json = database.json()

print("O livro buscado foi: " ,json["title"])
print("A editora é: " ,json["publishers"])