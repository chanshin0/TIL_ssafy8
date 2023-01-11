# 최소합
def dfs(i, j, k):
    global minV
    if k > minV:
        return

    if [i, j] == [N-1, N-1]:
        if k < minV:
            minV = k
        return

    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < N:
            dfs(ni, nj, k+arr[ni][nj])

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    delta = [[0,1],[1,0]]
    minV = 100000000
    dfs(0, 0, arr[0][0])
    print(f'#{tc+1} {minV}')