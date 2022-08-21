# 풍선팡
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # [[2, 1, 1, 2, 2], [2, 2, 1, 2, 2], [2, 2, 1, 1, 2]]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    ismax = 0
    for i in range(N):
        for j in range(M):
            pop = arr[i][j]
            for d in range(len(dx)): # 0 1 2 3
                for p in range(1, arr[i][j]+1): # 풍선에 들어있는 번호
                    di = i + dx[d]*p
                    dj = j + dy[d]*p
                    if 0 <= di < N and 0 <= dj < M:
                        pop += arr[di][dj]

            if pop > ismax:
                ismax = pop

    print(f'#{tc+1} {ismax}')