# 조합 1
# N = 10
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             print(i, j ,k)
#

def comb(n, r, s):
    if r == 0:
        print(*com[::-1])
    else:
        for i in range(s, n-r+1):
            com[r-1] = a[i]
            comb(n, r-1, i+1)

def pi(n, r, s):
    if r == s:
        print(*com[::-1])
    else:
        for i in range(n):
            com[s] = a[i]
            pi(n, r, s+1)

def perm(n, r, k):
    if r == 0:
        print(*com[::-1])
        # com = [0] * r
    else:
        for i in range(n):
            if a[i] not in com:
                com[r-1] = a[i]
                perm(n, r-1, k)
            if i == n-1 and r == k:
                com[r-1] = a[i]
                perm(n, r-1, k)


a = [1,2,3]
n = 3
r = 2
# com = [0]*r
# comb(n, r, 0)
# print('```````````````````````````')
com = [0]*r
pi(n ,r, 0)
# print('```````````````````````````')
# com = [0]*r
# perm(n, r, r)