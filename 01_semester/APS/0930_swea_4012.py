# 요리사
def ncr(n, r, s):
    if r == 0:
        a = comb[:]
        comb_foods.append(a)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = foods[i]
            ncr(n, r-1, i+1)

T = int(input())
for tc in range(T):
    N = int(input())
    ajdM = [list(map(int, input().split())) for _ in range(N)]
    foods = list(range(N))
    comb = [0]*(N//2)
    comb_foods = []
    ncr(N, N//2, 0)
    # [[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [3, 2]]



