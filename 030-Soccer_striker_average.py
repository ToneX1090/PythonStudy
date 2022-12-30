lists = [["Xulapa",3,0,1,1],["Dodo",2,1,1,2],["Didico",1,4,1,2],["Galinho",2,4,2,2]]
dict = {}
sort_dict = {}

for list in range(len(lists)):
    nome = lists[list][0]
    gols = lists[list][1:]
    media = sum(gols) / len(gols)
    dict[nome] = media
    sort_dict = sorted(dict, key = dict.get, reverse=True)

print(dict)
print(sort_dict)

#     sort_dict = sorted(dict, key = dict.get, reverse=True)

#     for striker in sort_dict:
#         final_striker[striker] = media

# print(final_striker)

# for striker in sorted(dict, key = dict.get, reverse=True):
#     final_strikers = striker

# print(final_strikers[:3])