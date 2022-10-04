# 최소 이동 거리
from collections import deque
T = int(input())
for tc in range(T):
    N, E = map(int, input().split())
    adjL = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        adjL[a].append([b,c])
    # [[[1, 1], [2, 6]], [[2, 1]], []]

    dists = [11]*(N+1)
    dists[0] = 0
    que = deque([[0,0]])
    while que:
        f, w = que.popleft()

        if adjL[f]:
            for n, w in adjL[f]:
                d = dists[f] + w    # n까지의 이동거리
                if d < dists[n]:
                    dists[n] = d
                    que.append([n, w])
    print(f'#{tc+1} {dists[N]}')