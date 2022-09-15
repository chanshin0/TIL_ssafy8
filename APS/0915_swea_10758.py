# 이진 힙
# 부모 노드의 값<자식 노드의 값 ->  최소 힙

T = int(input())
for tc in range(T):
    N = int(input())
    entree = list(map(int, input().split()))    # 진입시킬 리스트
    tree = [0]+[entree[0]]                      # 루트넣고 차례로 진입

    for i in range(1, N):
        tree.append(entree[i])
        j = tree.index(entree[i])               # 새로 들어온 노드번호
        while j != 1:
            if tree[j//2] > tree[j]:            # 부모 노드값이 자식 노드보다 크면 스위치
                tree[j//2], tree[j] = tree[j], tree[j//2]
                j = j//2
            else:                               # 스위치할 것 없으면 종료
                break

    ans = 0
    last = N            # 맨 마지막 노드 번호
    while True:         # 루트까지 조상노드 ans에 더하기
        ans += tree[last//2]
        last //= 2
        if last == 1:
            break
    print(f'#{tc+1} {ans}')

