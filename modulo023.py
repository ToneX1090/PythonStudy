import sys
import requests

def function_ISBN():

    ISBN = sys.argv[1]
    database = requests.get("https://openlibrary.org/isbn/"+ISBN+".json")
    json = database.json()

    print("\nResumo: " ,json["description"])
