a = [1, 2, 3]
b = [[] for _ in range(3**2)]
print(b)
# 11 12 13 21 22 23 31 32 33
# 111 112 113 121 122 123 131 132 133
c = []
n = 2
for i in a: # 1 2 3
    for j in a: # 1 2 3
        if a+b == a[-1]:
            c.append([i, j])
# print(c)

# while True:
for i in a: # 1 2 3
    for j in b[:i*3]: #
        j.append(i)
print(b)
