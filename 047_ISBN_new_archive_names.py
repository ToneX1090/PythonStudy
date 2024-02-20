import sys
import requests

def title_name(ISBN):

    database = requests.get("https://openlibrary.org/isbn/"+ISBN+".json")
    json = database.json()

    print("\nTitulo -" ,json["title"] ,json["subtitle"])

title_name()