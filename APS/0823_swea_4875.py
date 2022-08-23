# [기본] 5일차 - 미로 (제출용)

def f(i, j ,N):             # 도착여부를 확인하는 재귀하수, 중복방문 불필요
    if maze[i][j] == 3:     # 도착
        return 1
    else:
        maze[i][j] == 1
        for di, dj in []:
            ni, nj = i+di, j+dj
            if 0 <= ni <3 and 0 <= nj <3 and maze[nj[nj] != 1:
                if f(ni, nj N)

T = int(input())
for tc in range(T):
    N = int(input())
    maza = [list(map(int, input().split())) for _ in range(N)]

    # 시작점 찾기
    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j # 함수로 보내?
                break