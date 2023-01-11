# 파스칼의 삼각형
T = int(input())
for tc in range(T):
    N = int(input())

    arr = []
    for i in range(1,N+1): # 1 2 3 4
        arr.append([1]*i)
    # print(arr)

    for i in range(2, N): # 2 3
        for j in range(1, i): # 21 31 32
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    # print(arr)
    print(f'#{tc+1}')
    for i in range(N):
        print(*arr[i])
