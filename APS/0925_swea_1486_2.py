# 비트연산으로 부분집합구하는 풀이

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    employees = list(map(int, input().split()))
    n = len(employees)

    ismin = 10000000
    for i in range(1<<n):   # 부분집합의 개수는 총 2**n개
        mysum = 0
        for j in range(n):  # 0번부터 n-1번 비트에 대해서
            if i&(1<<j):    # i의 j번째 비트가 1이라면
                mysum += employees[j]    # 그 비트에 해당하는 원소는 부분집합
        if mysum >= B:
            if mysum < ismin:
                ismin = mysum

    print(f'#{tc+1} {ismin-B}')


