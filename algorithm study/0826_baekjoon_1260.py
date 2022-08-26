# DFS와 BFS
def bfs(V, N):
    visited = [0]*(N+1)
    visited[V] = 1
    q = [V]
    bfs = [V]
    while q:
        front = q.pop(0)
        for w in node[front]: # 2 3 4
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[front] + 1
                bfs.append(w)
    return bfs

def dfs(V, N):
    visited = [0] * (N + 1)
    visited[V] = 1
    stack = [V]
    dfs = [V]
    while stack:
        top = stack.pop()
        if node[top]:
            move = node[top].pop(0)     # 작은 것부터 탐색하라는 조건
            if visited[move] == 0:
                stack.append(move)
                dfs.append(move)
                visited[move] = 1

    return dfs

N, M, V = map(int, input().split())
node = [[] for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for i in node:
    i.sort()
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3], []]
# [[], [2, 3, 4], [4], [4], [], []]

b = bfs(V, N)
a = dfs(V, N)
print(*a)
print(*b)

