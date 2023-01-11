# 보급로
from collections import deque
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    costs = [[1000]*N for _ in range(N)]
    delta = [[0,1],[1,0],[0,-1],[-1,0]]

    que = deque([[0, 0]])
    costs[0][0] = 0
    while que:
        si, sj = que.popleft()
        for di, dj in delta:
            ni, nj = si+di, sj+dj
            # 여기서 델타 최소값 저장
            if 0 <= ni < N and 0 <= nj < N:
                cost = costs[si][sj] + arr[ni][nj]
                if costs[ni][nj] > cost:
                    costs[ni][nj] = cost
                    que.append([ni, nj])

    print(f'#{tc+1} {costs[N-1][N-1]}')