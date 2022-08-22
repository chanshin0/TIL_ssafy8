# 색칠하기2
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]

    # 칠하기
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for di in range(r2-r1+1): # 0 1 2
            for dj in range(c2-c1+1): # 0 1 2
                if arr[r1+di][c1+dj] == 0:          # 칠 안된 곳이면 칠하고
                    arr[r1+di][c1+dj] = color
                else:
                    arr[r1 + di][c1 + dj] = 0      # 칠 돼있는 곳이면 0으로
    # print(arr)
    cnt = ans = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] != 0:  # 칠 돼있는 영역일 때
                ans += 1        # 개수 세고
                if i+1 < 10:
                    if arr[i+1][j] != 0:
                        cnt += 1
                if j+1 < 10:
                    if arr[i][j+1] != 0:
                        cnt += 1
                if 0 <= i-1:
                    if arr[i-1][j] != 0:
                        cnt += 1
                if 0 <= j-1:
                    if arr[i][j-1] != 0:
                        cnt += 1
    # print(ans, cnt)
    print(f'#{tc} {(ans*4)-cnt}')