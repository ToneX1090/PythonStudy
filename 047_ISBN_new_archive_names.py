import sys
import requests

def title_name(ISBN):

    database = requests.get("https://openlibrary.org/isbn/"+ISBN+".json")
    json = database.json()

    title = json["title"]
    Subtitle = json["subtitle"]
    
    #print("\nTitulo -" ,json["title"] ,json["subtitle"])
title_name()

archive=open(sys.argv[1], "r")
books = archive.readlines()

newarchive = open("Booktitles.txt" , "w")
    
for book in books:
    newarchive.write("\nTitulo -" ,json["title"] ,json["subtitle"]
newarchive.close()