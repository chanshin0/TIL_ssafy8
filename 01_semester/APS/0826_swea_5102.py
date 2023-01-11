# 5102. 노드의 거리 (제출용)
def bfs (s, g, V):
    v = [0]*(V+1)               # 1~V번까지의 노드
    v[s] = 1                    # 시작 지점 1 (되돌아오는것 방지)
    q = [s]                     # 큐 생성, 시작점 인큐
    while q:
        move = q.pop(0)             # 디큐
        if move == g:               # 도착지 찾았으면 종료
            return v[move] - 1
        else:
            for w in node[move]:    # 디큐한 노드에 연결 된 길 bfs 탐색
                if v[w] == 0:       # 방문 안한 곳이면
                    q.append(w)     # 방문 하고
                    v[w] = v[move] + 1  # 경로 체크
    return 0                        # 모든 경로를 다 돌았는데 도착지 못만났으면 종료


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]

    for e in range(E):
        s, g = map(int, input().split())
        node[s].append(g)
        node[g].append(s)
    S, G = map(int, input().split())

    print(f'#{tc+1} {bfs(S, G, V)}')

