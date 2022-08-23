T = int(input())
for tc in range(T):
    N = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    f_sum = 0
    box = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            f_sum += arr[i][j]
            box += 1
    f_avg = f_sum // box # 2

    ans = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            cnt = f_avg - arr[i][j]
            if cnt > 0:
                ans += cnt
            elif cnt < 0:
                ans += (-1)*cnt
            else:
                continue
    print(f'#{tc+1} {ans}')
