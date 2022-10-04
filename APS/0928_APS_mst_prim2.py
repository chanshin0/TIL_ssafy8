# prim 좀 더 쉬운 버전
def prim1(r, V):
    MST = [0]*(V+1)         # MST 포함여부
    MST[r] = 1              # 시작 정점 표시
    s = 0                   # MST 가중치의 합

    for _ in range(V):      # V+1개의 정점 중 V개를 선택
        u = 0
        minV = 10000
        for i in range(V+1):        # MST에 포함된 정점 i와 인접한 정점j 중 MST에 포함될 정점 구하기(간선의 가중치가 제일 작은애)
            if MST[i] == 1:
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1          # 정점 u를 MST에 추가

    return s      # MST 가중치의 합합


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