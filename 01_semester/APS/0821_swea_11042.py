# 부분 배열의 합
T = int(input())
for tc in range(T):
    N, n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ismax = 0
    for i in range(N):
        for j in range(N):
            myBox = 0
            for di in range(n): # 0 1 2
                for dj in range(m): # 0 1 2
                    if 0 <= i+di < N and 0 <= j+dj < N:
                        myBox += arr[i+di][j+dj]

            if myBox > ismax:
                ismax = myBox
    print(f'#{tc+1} {ismax}')