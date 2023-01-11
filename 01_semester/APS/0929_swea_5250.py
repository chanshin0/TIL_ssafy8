# 최소 비용
from collections import deque

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    costs = [[100000]*N for _ in range(N)]
    delta = [[0,1],[1,0],[0,-1],[-1,0]]

    que = deque([[0,0]])
    costs[0][0] = 0
    while que:
        fi, fj = que.popleft()

        for di, dj in delta:
            ni, nj = fi+di, fj+dj
            if 0 <= ni < N and 0 <= nj < N:
                h = arr[ni][nj] - arr[fi][fj]     # 인접 칸과의 높이 차
                if h > 0:                         # 높이가 높아진다면
                    cost = costs[fi][fj] + h + 1    # [ni,nj]까지 이동하는 비용
                else:
                    cost = costs[fi][fj] + 1
                if cost < costs[ni][nj]:            # 원래 저장돼있던 값보다 작다면
                    costs[ni][nj] = cost            # 재 할당
                    que.append([ni,nj])
    print(f'#{tc+1} {costs[N-1][N-1]}')