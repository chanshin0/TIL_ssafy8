def dfs(v):
    visited[v] = 1
    if v == 99:
        return 1

    for n in node[v]:
        if visited[n] == 0: # 아직 방문 안한 곳이면
            visited[n] = 1
            dfs(n)

T = 10
for tc in range(T):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    # [0, 1, 0, 2, 1, 4, 1, 3, 4, 8, 4, 3, 2, 9, 2, 5, 5, 6, 5, 7, 7, 99, 7, 9, 9, 8, 9, 10, 6, 10, 3, 7]

    node = [[] for _ in range(100)]
    for i in range(0, len(arr), 2):
        node[arr[i]].append(arr[i+1])
    # print(node)
    # [[1, 2], [4, 3], [9, 5], [7], [8, 3], [6, 7], [10], [99, 9], [], [8, 10], [], [], [], [], [], [], [], [], []

    visited = [0]*100
    dfs(0)

    print(f'#{tc} {visited[99]}')
    # dfs함수 재귀로 풀이