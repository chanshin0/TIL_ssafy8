words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}
im_lst = ['b','m','p']
lst = []
for word in words_dict.keys():
    if word[0] in im_lst:
        word = 'im'+word
        lst.append(word)
    elif word[0] == 'l':
        word = 'il'+word
        lst.append(word)
    elif word[0] == 'r':
        word = 'ir'+word
        lst.append(word) 
    else:
        word = 'in'+word
        lst.append(word) 
print(sorted(lst))

# ws_5_5와 같음