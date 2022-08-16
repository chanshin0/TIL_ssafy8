#파리 퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ismax = 0
    for i in range(N):
        for j in range(N):
            for k in range(-M+1, M): # -2, -1, 1, 2
                if k == 0:
                    continue
                if 0 <= i+k < N and 0 <= j+k < N:
                    sum_t = arr[i][j]
                    sum_t += arr[i+k][j] + arr[i][j+k] # 십자모양
                    sum_x = arr[i][j]
                    sum_x += arr[i+k][j+k] + arr[i+k][j-k] # X모양
                elif i+k < 0:
                    pass
                elif i+k >= N:
                    pass
                elif j+k < 0:
                    pass
                elif j+k >= N:
                    pass
            if sum_t > ismax:
                ismax = sum_t
            if sum_x > ismax:
                ismax = sum_x

    print(ismax)