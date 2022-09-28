# 크루스칼..
def find_set(x):
    while x != rep[x]: # 자기 자신이 대표일때까지
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])      # w기준으로 정렬할려고 앞에다 놓음. or 람다 사용
edge.sort(key=lambda x:x[2])
rep = [i for i in range(V+1)]   # 대표원소 배열

N = V + 1   # 실제 정점의 개수
cnt = 0     # 선택한 edge의 수
total = 0   # MST 가중치의 합
for u, v, w in edge:
    if find_set(u) != find_set(v):  # 사이클이 만들어지는 간선을 거르기 위한 조건
        cnt += 1
        union(u, v)
        total += w
        if cnt == N-1:              # 간선 수, 다 골랐으면 종료
            break

print(total)