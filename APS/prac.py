a = [1,2,3,4,5,9,3,10,0,0,0,0]

for i in range(1,len(a)):
    if a[i] < a[i-1]:
        a[i] = a[i-1]
# a[0] += 1
# a[-1] -= 1
print(a)
