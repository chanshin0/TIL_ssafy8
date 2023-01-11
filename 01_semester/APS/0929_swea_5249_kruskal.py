# 최소 신장 트리
# 크루스칼
def find_set(x):
    while rep[x] != x:      # 자기 자신이 대표원소가 나올떄까지
        x = rep[x]          # x에 x의 대표원소 재할당
    return x

def union(u, v):
    a = find_set(u)
    b = find_set(v)
    rep[b] = a

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x:x[2])
    rep = list(range(V+1))          # 0~V번까지 대표원소 할당할 배열

    total = 0                       # 가중치의 합
    cnt = 0                         # MST구성하는 간선 개수
    for u, v, w in edges:
        if find_set(u) != find_set(v):    # 사이클을 만들지 않는다면
            union(u, v)
            total += w
            cnt += 1                # (정점 개수 -1)개의 간선을 갖는다
            if cnt == V:            # 간선 개수에 도달하면 종료
                break

    print(f'#{tc+1} {total}')