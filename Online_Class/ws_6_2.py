grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

print(sorted(grain_lst, key=lambda x : x[1], reverse=True)[0][0])