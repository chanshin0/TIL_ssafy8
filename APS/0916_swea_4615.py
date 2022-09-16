# 재미있는 오셀로 게임
def run_Oth(i, j, c):
    othello[i][j] = c
    for di, dj in delta:                # 델타 탐색
        temp = []
        for m in range(1, N):           # 가능한 모든 범위 싹
            ni = i + di * m
            nj = j + dj * m
            if 'find!' in temp:             # 찾았으면 m은 그만돌려도됨
                break
            else:                           # 아직 못찾았으면 계속 탐색
                if 0 <= ni < N and 0 <= nj < N:
                    if othello[ni][nj] == 0:    # 탐색중 0만나면 종료
                        break
                    elif othello[ni][nj] == c:  # 같은 색 찾으면 종료
                        temp.append('find!')
                        break
                    else:                       # 다른 색이면 temp에 저장
                        temp.append([ni,nj])
        if 'find!' in temp:                 # 탐색 종료 후 찾았는지 판별
            for ti, tj in temp[:-1]:        # 색깔 바꿔주기
                othello[ti][tj] = c

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    my_turn = []
    for i in range(M):
        a, b, c = map(int, input().split())
        if c == 1:                          # c가 1이면 흑돌
            my_turn.append([b-1, a-1, 'B'])
        else:                               # c가 2이면 백돌
            my_turn.append([b-1, a-1, 'W'])

    othello = [[0]*(N) for _ in range(N)]
    othello[N//2-1][N//2-1] = othello[N//2][N//2] = 'W'
    othello[N//2-1][N//2] = othello[N//2][N//2-1] = 'B'

    delta = [[0,1],[1,0],[0,-1],[-1,0],[-1,1],[1,1],[1,-1],[-1,-1]]

    while my_turn:                      # my_turn에서 앞에부터 pop하면서
        i, j, c = my_turn.pop(0)        # 오셀로 게임 돌리기
        run_Oth(i, j, c)

    B = 0
    W = 0
    for i in range(N):
        for j in range(N):
            if othello[i][j] == 'B':
                B += 1
            if othello[i][j] == 'W':
                W += 1

    print(f'#{tc+1} {B} {W}')

