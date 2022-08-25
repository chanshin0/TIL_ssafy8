# [S/W 문제해결 기본] 7일차 - 미로1
def bfs (i, j, N):
    stack = [(i, j)] # 출발점에서 시작
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    if maze[i][j] == 3:
        return 1
    else:
        while stack:
            i, j = stack.pop()
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and  visited[ni][nj] == 0: # 범위 내에 있고, 벽이 아니며, 방문하지 않은 곳일때
                    stack.append((i, j))
                    visited[ni][nj] = 1

T = 1
for tc in range(T):
    tc = input()
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]


    sti = stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j

    print(f'#{tc} {f(sti, stj, N)}')
