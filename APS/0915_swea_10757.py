# 이진탐색
def inorder(n):
    global i
    if n<=N:                    # 중위순회하면서
        inorder(n*2)
        if com_bi_tree[n]:      # 완전이진트리의 노드가 존재하면
            tree[n] = i         # 1씩 더해줌
            i += 1
        inorder(n*2+1)

T = int(input())
for tc in range(T):
    N = int(input())
    i = 1

    com_bi_tree = list(range(N+1))  # 완전이진트리
    tree = [0]*(N+1)                # 새로 값을 담을 트리

    inorder(1)
    print(f'#{tc+1} {tree[1]} {tree[N//2]}')