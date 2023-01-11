# 장훈이의 높은 선반
def f(i, N):
    if i == N:
        sum = 0
        for i in range(N):
            if bit[i] == 1:
                sum += employees[i]
        if sum >= B:
            top.append(sum)

    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    employees = list(map(int, input().split()))

    bit = [0]*N
    ismin = 1000000000
    top = []
    f(0, N)

    print(f'#{tc+1} {min(top)-B}')