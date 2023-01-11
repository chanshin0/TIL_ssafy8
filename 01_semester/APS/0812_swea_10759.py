# 색칠하기2
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]

    # 칠하기
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for di in range(r1, r2+1): # 2 3 4
            for dj in range(c1, c2+1): # 2 3 4
                if arr[di][dj] == 0:          # 칠 안된 곳이면 칠하고
                    arr[di][dj] = color
                else:
                    arr[di][dj] = 0      # 칠 돼있는 곳이면 0으로
    # print(arr)

    cnt = 0
    dt = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(10):
        for j in range(10):
            if arr[i][j] != 0:  # 칠 돼있는 영역일 때
                for dx, dy in dt:
                    di = i + dx
                    dj = j + dy
                    if 0 <= di < 10 and 0 <= dj < 10:
                        if arr[di][dj] != arr[i][j]:
                            cnt += 1
                    else:
                        cnt += 1

    # print(ans, cnt)
    print(f'#{tc} {cnt}')