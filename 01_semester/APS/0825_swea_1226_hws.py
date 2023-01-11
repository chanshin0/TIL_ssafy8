# [S/W 문제해결 기본] 7일차 - 미로1
def bfs (i, j, N):
    q = [(i, j)]                            # 큐 생성 & 인큐
    visited = [[0]*N for _ in range(N)]     # v 생성
    visited[i][j] = 1                       # 시작점 인큐됨 표시

    while q:
        i, j = q.pop(0)                   # 디큐(앞에서부터)
        if maze[i][j] == 3:
            return 1
        else:
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and  visited[ni][nj] == 0:
                                                # 범위 내에 있고, 벽이 아니며, 방문하지 않은 곳일때,
                    q.append((ni, nj))          # 방문해라 (인큐)
                    visited[ni][nj] = 1         # 인큐되었다고 표시
    return 0                                 # 전부 탐색마쳤는데도, 리턴 1 만나지 못했다면 0

def dfs(i, j, N):
    # global answer
    if maze[i][j] == 3:
        # answer = 1
        return 1
    else:
        maze[i][j] = 1
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:
                if dfs(ni, nj, N):
                    return 1
        return 0            # 진행방향에서 3을 못찾은 경우

T = 10
for tc in range(T):
    tc = input()
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]

    sti = stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j

    # print(f'#{tc} {bfs(sti, stj, N)}')
    # answer = 0
    # dfs(sti, stj, N)
    print(f'#{tc} {dfs(sti, stj, N)}')