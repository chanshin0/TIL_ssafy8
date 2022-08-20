#파리 퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ismax = 0
    for i in range(N):
        for j in range(N):
            sum_t = arr[i][j] # 10자
            sum_x = arr[i][j] # x자
            for k in range(1, M): # 1 2
                if i + k < N and j + k < N and 0 <= i - k and 0 <= j - k:               # 아래
                    sum_t += arr[i+k][j]
                    sum_t += arr[i][j+k]
                    sum_t += arr[i-k][j]
                    sum_t += arr[i][j-k]
            if sum_t > ismax:
                ismax = sum_t

            # x자
            for h in range(1, M): # 1 2
                if i + h < N and j + h < N and 0 <= j - h and 0 <= i - h:     # 우하단
                    sum_x += arr[i+h][j+h]
                    sum_x += arr[i+h][j-h]
                    sum_x += arr[i-h][j-h]
                    sum_x += arr[i-h][j+h]
            if sum_x > ismax:
                ismax = sum_x

    print(f'#{tc} {ismax}')
    # 0821 품.