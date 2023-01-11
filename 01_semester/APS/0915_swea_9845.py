# 노드의 합
def postorder(n):
    if n<=N:
        postorder(n*2)
        postorder(n*2+1)
        a = tree[n]             # tree[n]값을 저장 후,
        if a and n > 1:         # a가 반환 되면
            tree[n//2] += a     # 부모 노드에다가 더해줌

T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for i in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    postorder(1)
    print(f'#{tc+1} {tree[L]}')


