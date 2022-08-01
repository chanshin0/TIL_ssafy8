n = [4,4,7,8,10,4]
lst = []
for i in n:
    if n.count(i) == 1:
        lst.append(i)
print(sum(lst))