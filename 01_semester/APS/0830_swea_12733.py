# 기지국
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    dt = [[0,1],[1,0],[0,-1],[-1,0]]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                for di, dj in dt:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'
            elif arr[i][j] == 'B':
                for di, dj in dt:
                    for k in [1,2]:
                        ni = i + di*k
                        nj = j + dj*k
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'H':
                                arr[ni][nj] = 'X'
            elif arr[i][j] == 'C':
                for di, dj in dt:
                    for k in [1, 2, 3]:
                        ni = i + di * k
                        nj = j + dj * k
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'H':
                                arr[ni][nj] = 'X'
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{tc+1} {cnt}')
