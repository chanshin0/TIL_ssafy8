# 상호배타집합, 서로소 집합

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    # r1 = find_set(x)
    # r2 = find_set(y)
    # p[r2] = r1
    p[find_set(y)] = find_set(x)


# make set
p = list(range(7))

union(3, 4)
union(5, 6)
union(4, 6)
print(p)
