A = list(range(1, 13))
T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    result = []
    # 부분집합 비트연산
    for i in range(1<<len(A)):
        s = [] # 부분집합 담기고, i돌때마다 result에 담고 초기화
        for j in range(len(A)):
            if i & (1<<j): # j번 비트가 1이면 arr[j]가 부분집합에 포함
                s.append(A[j])
        if len(s) == N and sum(s) == K:
            result.append(s)

    print(f'#{tc+1} {len(result)}')