# N-Queen
def make_candidate(a, i, N):
    for j in range(N):
        chk = 0
        for di, dj in [[-1,1],[-1,0],[-1,-1]]:
            ni, nj = i+di, j+dj
            while 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 1:              # 1만나서 종료
                    break
                ni += di
                nj += dj
            if 0 <= ni < N and 0 <= nj < N:     # while문 종료가 1만나서 끝났으면(while문이 종료되었는데 아직도 ni와 nj가 범위 내에 있다는 것은 'while문 내의 종료조건'에 의해 종료되었음을 의미함)
                break                               # 델타탐색 종료
            else:                               # while문이 정상 종료 됐으면
                chk += 1                            # 그 방향 ok
        if chk == 3:                                # 3방향 다 ok이면
            a.append(j)                             # 후보에 추가

def f(i, N):
    global cnt
    if i == N:       # 마지막 행까지 queen을 놓은 경우
        cnt += 1
    else:
        cands = []
        make_candidate(cands, i, N)
        for j in cands:
            board[i][j] = 1     # queen을 놓음
            f(i+1, N)
            board[i][j] = 0     # 다른 위치에 놓기 위해 치움

T = int(input())
for tc in range(T):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    cnt = 0
    f(0, N)

    print(f'#{tc+1} {cnt}')
