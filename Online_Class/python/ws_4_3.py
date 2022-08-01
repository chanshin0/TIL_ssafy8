a = [1, 1, 3, 3, 0, 1,1,1,1,2,2,2,1]
lst = []

for i, n in enumerate(a):
    if i <= len(a)-2:
        if n != a[i+1]:
            lst.append(n)
lst.append(a[len(a)-1])
print(lst)