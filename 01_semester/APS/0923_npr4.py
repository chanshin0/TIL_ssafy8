# used를 사용하는데 이번에는 N개의 원소 중에서 R개만 사용하는 경우
def f(i, k, r):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1, k, r)
                used[j] = 0


N = 3
R = 5
a = [i for i in range(1, N+1)]
used = [0]*N
p = [0]*R
f(0, N, R)