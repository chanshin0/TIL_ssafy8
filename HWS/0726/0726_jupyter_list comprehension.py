def dict_invert(my_dict):
    key_lst = list(my_dict.keys())
    val_lst = list(my_dict.values())

    new_dict = {}
    for i in range(len(val_lst)):
        if val_lst.count(val_lst[i]) != 1: # 중복된 value값이 있으면
            a = [k for k, v in my_dict.items() if val_lst.count(v) != 1] # 리스트로 만든다 <--
            new_dict.setdefault( val_lst[i], a)
        else:    
            new_dict.setdefault( val_lst[i], [key_lst[i]]) 
    return new_dict

print(dict_invert({1: 10, 2: 20, 3: 30}))
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
print(dict_invert({1: True, 2: True, 3: True}))