password = input("Digite uma contrasenha forte que com mais de 8 caracteres: ")

if len(password) < 8:
       #print("A contrasenha não possui uma letra maiuscula, por favor, tente novamente!") 
    print("A contrasenha informada tem menos de 8 caracteres, por favor, tente novamente!")
else:
    '''
    #verificar se contem maiuscula
    if not any(c.isupper() for c in password):
    
    #verificar se contem minuscula
    if not any(c.islower() for c in password):
    
    #verificar se contem #%$%$#%
    if not re.search(r'[#!@%&$]', password):
    
    #verificar se contem numeros
    if not any(c.isdigit() for c in password):
    '''

    else:
        print("Nivel de contrasenha fraca!")