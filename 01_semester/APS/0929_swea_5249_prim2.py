# 최소 신장 트리
# 프림

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    adjM = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        adjM[a][b] = c
        adjM[b][a] = c

    print(adjM)