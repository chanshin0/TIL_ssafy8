# 토글
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0 # 1의 개수 카운트
    k = 0
    while k != M:
        k += 1
        for i in range(N): # 0 1 2 3 4
            for j in range(N): # 0 1 2 3 4
                if M % k == 0:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                        if k == M: # 맨 마지막 토글 때 1로 변환한 것 카운트
                            cnt += 1
                    else:
                        arr[i][j] = 0
                elif (i+1)+(j+1) == k or (i+1+j+1) % k == 0:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    else:
                        arr[i][j] = 0
        # print(arr)

    print(f'#{tc} {cnt}')