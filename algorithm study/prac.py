def inorder(n):
    if 0 < n <= V:
        return inorder(2 * n) + tree[n] + inorder(2 * n + 1)
    else:
        return ''


T = 10
for tc in range(1, T + 1):
    V = int(input())  # 정점 수
    tree = [0] * (V + 1)  # 정점 문자

    # 완전 이진 트리 저장
    for _ in range(V):
        n, s, *c = input().split()
        tree[int(n)] = s


    root = 1
    result = inorder(root)
    print(f'#{tc} {result}')