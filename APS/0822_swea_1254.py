# 달팽이 숫자
T = int(input())
for tc in range(T):
    N = int(input())
    house = [[0]*N for _ in range(N)] # 달팽이집

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    snail = 1
    i = j = k = 0
    while snail <= N*N:
        if house[i][j] == 0:
            house[i][j] = snail
            snail += 1
            i += dx[k]
            j += dy[k]
            if 0 <= i < N and 0 <= j < N and house[i][j] == 0:
                continue
            else:
                i -= dx[k]
                j -= dy[k]     # 범위 벗어나면 빽
        else:
            k = (k+1) % 4       # 방향전환하고 i,j 재설정
            i += dx[k]
            j += dy[k]
        # print(house)

    print(f'#{tc+1}')
    for i in range(N):
        print(' '.join(map(str, house[i])))