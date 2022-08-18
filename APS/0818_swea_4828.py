# 1일차 - min max (제출용)
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    ismax = 0
    ismin = arr[0]
    for i in arr:
        if i > ismax:
            ismax = i
        if i < ismin:
            ismin = i

    print(f'#{tc+1} {ismax-ismin}')