# N-Queen
def valid(i, j):
    for n in range(N):
        if board[i][n] == 1:
            return 0
        if board[n][j] == 1:
            return 0
    for di, dj in delta2:
        ni, nj = i+di, j+dj
        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj] == 1:
                return 0
            ni += di
            nj += dj
    return 1

def dfs(i, j):
    global cnt
    if cnt == N:
        return
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:
            if valid(ni, nj):
                board[ni][nj] = 1
                cnt += 1
                dfs(ni, nj)
        if cnt == N:
            break


T = int(input())
for tc in range(T):
    N = int(input())
    board = [[0] * N for _ in range(N)]

    ans = 0
    delta = [[1,2],[1,-2],[2,-1],[2,1],[-1,2],[-1,-2],[-2,-1],[-2,1]]
    delta2 = [[-1,1],[-1,-1]]
    k = 0
    while k != N:
        board[0][k] = 1
        cnt = 1
        dfs(0, k)
        if cnt == N:
            ans += 1
        k += 1
        board = [[0] * N for _ in range(N)]

    print(f'#{tc+1} {ans}')
