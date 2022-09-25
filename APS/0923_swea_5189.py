# 전자 카트
def f(i, k):
    if i == k:
        mysum = 0
        for i in range(N): # 0 1 2
            mysum += arr[i][p[::-1][i]-1]
            print(p[::-1][i])
        fee.append(mysum)

    else:
        for j in range(k):
            if used[j] == 0:    # a[j]가 아직 사용되지 않았으면
                used[j] = 1
                p[i] = a[j]
                f(i+1, k)       # 다음 인덱스 정하러 보냄
                used[j] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    a = [i for i in range(1, N+1)]
    used = [1] + [0] * (len(a)-1)
    p = [1] + [0] * (len(a)-1)

    fee = []
    f(1, 3)
    print(fee)