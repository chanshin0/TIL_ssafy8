# 하나로
def prim(r, v):             # 시작정점, 마지막 정점 0, 3
    mst = [0]*N
    mst[r] = 1
    s = 0

    for _ in range(N-1):    # n개의 정점 중 n-1개를 선택
        u = 0
        minV = 1000000**2+1
        for i in range(N):
            if mst[i] == 1:     # mst의 정점에 붙은 가지 중에 최소값인것을 찾음
                for j in range(N):
                    if adjM[i][j] > 0 and minV > adjM[i][j] and mst[j] == 0:
                        u = j
                        minV = adjM[i][j]
        mst[u] = 1
        s += minV
    return s

T = int(input())
for tc in range(T):
    N = int(input())
    lo_x = list(map(int, input().split()))
    lo_y = list(map(int, input().split()))
    E = float(input())

    adjM = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            length = (lo_x[i]-lo_x[j])**2 + (lo_y[i]-lo_y[j])**2
            adjM[i][j] = length*E

    # [[0, 10000, 160000, 170000], [0, 10000, 160000, 170000], [320000, 250000, 160000, 90000],
    #  [320000, 250000, 160000, 90000]]
    a = prim(0, N-1)
    print(f'#{tc+1} {round(a)}')