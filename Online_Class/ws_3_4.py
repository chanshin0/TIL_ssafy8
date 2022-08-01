blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

dict = {}
for i in set(blood_types):
    dict.setdefault(i, blood_types.count(i))
print(dict)

# ws_6_4와 같음
