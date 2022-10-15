
import requests

image = open("sapocururu.jpg","wb")
## https://upload.wikimedia.org/wikipedia/commons/b/be/Red_eyed_tree_frog_edit2.jpg > URL válida


try:

    response = requests.get("http://miltinho.com/imagemquenaoexiste.jpg")
    image.write(response.content)
    image.close()
    print("download concluido.")

except:
    print("URL não existe.")


#from urllib import request

#remote_url = "https://upload.wikimedia.org/wikipedia/commons/b/be/Red_eyed_tree_frog_edit2.jpg"

#local_file = "/Users/Milton/Pictures/pythontest.jpg"

#request.urlretrieve(remote_url, local_file)

#print("download concluido.")


