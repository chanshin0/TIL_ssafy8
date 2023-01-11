# 각 행의 구간합
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ismax = 0
    for i in range(N):
        pre_sum = 0
        for j in range(i, i+K):
            if j < N:                   # j가 범위 내에 있을 때
                pre_sum += arr[i][j]    # 구간합
        if ismax < pre_sum:
            ismax = pre_sum

    print(f'#{tc+1} {ismax}')
