# n개에서 r개를 고르는 조합(재귀)
import time
def ncr(n, r, s):   # s: 시작할 인덱스 위치
    if r == 0:                   # r-1번째 인덱스 ~ 0까지(맨뒤~맨앞)
        print(*comb[::-1])
    else:
        for i in range(s, n-r+1):
            comb[r-1] = a[i]     # 뒤에서부터 채움
            ncr(n, r-1, i+1)

a = [1,2,3,4,5]
n = len(a)
r = 3
comb = [0]*r
ncr(n, r, 0)


