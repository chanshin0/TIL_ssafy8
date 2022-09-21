# 중위순회
def inorder(n):
    if n:
        inorder(chL[n])
        print(par[n][1], end= '')
        inorder(chR[n])

for tc in range(10):
    N = int(input())
    par = [[] for _ in range(N+1)]
    chL = [0]*(N+1)
    chR = [0]*(N+1)

    for i in range(N):
        arr = list(input().split())
        par[i+1] = (int(arr[0]), arr[1])
        if len(arr) == 3:
            chL[i + 1] = int(arr[2])
        elif len(arr) == 4:
            chL[i + 1] = int(arr[2])
            chR[i + 1] = int(arr[3])

    print(par)
    print(chL)
    print(chR)
    print(f'#{tc+1}', end=' ')
    inorder(1)
    print()
    # 중위순회