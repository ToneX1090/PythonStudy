lists = [["Xulapa",3,0,1,1],["Dodo",2,1,1,2],["Didico",1,4,1,2],["Galinho",2,4,2,2]]
dict_list = {}
c = 1

for list in range(len(lists)):
    nome = lists[list][0]
    gols = lists[list][1:]
    media = sum(gols) / len(gols)
    dict_list[nome] = media#dict

sort_dict = sorted(dict_list.items(), key=lambda item: item[1], reverse=True)#lista

striker_list = dict(sort_dict)

for k,v in striker_list.items():

    if c <= 3:

        print(f"O {c}º artilheiro é {k} com uma média de {v} gols")
        c = c + 1