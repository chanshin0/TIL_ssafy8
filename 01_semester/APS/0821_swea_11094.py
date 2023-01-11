# 가로 세로의 최대합
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    ismax = 0
    for i in range(N):
        for j in range(N):
            t_sum = arr[i][j]
            for k in range(len(dx)):  # 0 1 2 3
                for n in range(1, N): # 1 2 3
                    di = i + dx[k]*n  # N범위 내의 10자 합을 모두 계산해서
                    dj = j + dy[k]*n
                    if 0 <= di < N and 0 <= dj < N: # arr안에 있다면 합계 구함
                        t_sum += arr[di][dj]

            if t_sum > ismax:
                ismax = t_sum

    print(f'#{tc+1} {ismax}')
