# 그룹 나누기
def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x

def union(x, y):
    a = find_set(x) # 7
    b = find_set(y) # 4
    rep[b] = a
    # for i in range(1, N+1):
    #     if rep[i] == b:
    #         rep[i] = a

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    papers = list(map(int, input().split()))

    rep = list(range(N+1))
    for u in range(0, M*2, 2):
        v = u+1
        union(papers[u], papers[v])

    cnt = 0
    for i in range(1, N+1):
        if rep[i] == i:         # 대표원소일때 카운트
            cnt += 1
    print(f'#{tc+1} {cnt}')






