list_true = [1,2,3,4,5]
list_false = [1,2,2,3,4]

def verify(list):
    if len(list) == len(set(list)):
        print("A lista: ", list , "não tem elementos repetidos")
    else:
        print("A lista: ", list ,  "tem elementos repetidos, verifique")

verify(list_true)
verify(list_false)