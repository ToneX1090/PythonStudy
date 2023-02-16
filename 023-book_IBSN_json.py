import sys
import requests
import modulo023

def title_edit():

    ISBN = sys.argv[1]
    database = requests.get("https://openlibrary.org/isbn/"+ISBN+".json")
    json = database.json()

    print("\nO livro buscado foi: " ,json["title"])
    print("\nA editora é: " ,json["publishers"])

title_edit()
modulo023.function_ISBN()