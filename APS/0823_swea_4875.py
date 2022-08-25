# [기본] 5일차 - 미로 (제출용)

# def f(i, j ,N):             # 도착여부를 확인하는 재귀하수, 중복방문 불필요
#     if maze[i][j] == 3:     # 도착
#         return 1
#     else:
#         maze[i][j] = 1
#         for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:
#                 if f(ni, nj, N) == 1:
#                     return 1
#         return 0

def f(i, j, N):
    stack = [(i, j)] # 출발점 저장
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    while stack:
        i, j = stack.pop() # 꺼내서
        if maze[i][j] == 3:
            return 1
        else:
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    stack.append((ni, nj))
                    visited[ni][nj] = 1
    return 0

T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)

    # 시작점 찾기
    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j # 함수로 보내?
                break

    print(f'#{tc+1} {f(sti, stj, N)}')