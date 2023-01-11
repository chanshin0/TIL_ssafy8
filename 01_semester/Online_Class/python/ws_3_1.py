txt = 'apple,rottenBanana,apple,RoTTenorange,Orange'
input(txt)
a = txt.lower().split(',')
lst = []
for i in a:
    if 'rotten' in i:
        lst.append(i[6:])
    else:
        lst.append(i)

print(lst)

# ws_5_1과 같음