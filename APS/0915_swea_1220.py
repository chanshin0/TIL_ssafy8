# magnetic
T = 10
for tc in range(T):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    # 1번 자석이 나오면, 아래에 2번이 있고 그 사이에 1번 없으면 cnt += 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                for ti in range(i+1, N):
                    if table[ti][j] == 1:
                        break
                    elif table[ti][j] == 2:
                        cnt += 1
                        break

    print(f'#{tc+1} {cnt}')



