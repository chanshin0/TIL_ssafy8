#파리 퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ismax = 0
    dt_i = [0, 1, 0, -1]
    dt_j = [1, 0, -1, 0]
    dx_i = [1, 1, -1, -1]
    dx_j = [1, -1, 1, -1]
    for i in range(N):
        for j in range(N):
            sum_t = arr[i][j] # 10자
            sum_x = arr[i][j] # x자
            for m in range(1, M): # 1 2
                for h in range(len(dt_i)): # 0 1 2 3
                    di = i + dt_i[h]*m
                    dj = j + dt_j[h]*m
                    if 0 <= di < N and 0 <= dj < N:
                        sum_t += arr[di][dj]
            if sum_t > ismax:
                ismax = sum_t

            # x자
            for m in range(1, M):  # 1 2
                for h in range(len(dt_i)):  # 0 1 2 3
                    di = i + dx_i[h] * m
                    dj = j + dx_j[h] * m
                    if 0 <= di < N and 0 <= dj < N:
                        sum_x += arr[di][dj]
            if sum_x > ismax:
                ismax = sum_x

    print(f'#{tc} {ismax}')
