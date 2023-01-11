# 5105. [기본] 6일차 - 미로의 거리
def bfs(i, j, N):
    v = [[0]*N for _ in range(N)]   # v 생성
    q = []                          # q 생성 후 방문
    q.append([i, j])
    v[i][j] = 1                     # 방문 표시
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return v[i][j] - 2      # 출발지랑 도착지 제외한 칸 수 반환
        else:
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and v[ni][nj] == 0:
                    q.append([ni,nj])                 # 방문하고
                    v[ni][nj] = v[i][j] + 1           # 1(출발지)부터 하나씩 더하면서 표시
    return 0                                   # 끝까지 탐색 마쳤는데 도착지 못 만나면 0 반환

T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sti = stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j

    print(f'#{tc+1} {bfs(sti, stj, N)}')