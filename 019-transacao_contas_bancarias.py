transacoes = [["12345", 50], ["98765", -10], ["12345", -20], ["98765", 25]]

saldos = dict()

for transacao in transacoes:

    contatrans = transacao[0]
    valortrans = transacao[1]

    #verifica se a chave já existe no dicionario
    if contatrans in saldos:
        #se sim, soma
        saldos[contatrans] += valortrans
    else:
        #se não, atribui
        saldos[contatrans] = valortrans  

print (saldos)