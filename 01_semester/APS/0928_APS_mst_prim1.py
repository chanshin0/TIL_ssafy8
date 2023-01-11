def prim1(r, V):
    MST = [0]*(V+1)         # MST 포함여부
    key = [10000]*(V+1)     # 가중치의 최대값 이상으로 초기할당. key[v]는 v가 mst에 속한 정점과 연결될때 가중치
    key[r] = 0              # 시작정점의 key

    for _ in range(V):      # V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중 (mst에 아직 속하지 않고, key가 최소인) u찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1          # 정점 u를 MST에 추가

        # u를 MST에 넣고 인접한 최소 탐색
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:      # MST에 포함되지 않은 정점이고, u에 인접인 v에 대해,
                key[v] = min(key[v], adjM[u][v])    # u->v로 가는 간선의 가중치와 기존의 가중치의 최소값

    return sum(key)     # MST 가중치의 합합


V, E = map(int, input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]      # 인접행렬
# adjL = [[] for _ in range(V+1)]             # 인접 리스트

for _ in range(E):
    u ,v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w                       # 무향 그래프일 경우
    # adjL[u].append((v, w))
    # adjL[v].append((u, w))

    print(prim1(0, V)) # 시작정점, 마지막 정점