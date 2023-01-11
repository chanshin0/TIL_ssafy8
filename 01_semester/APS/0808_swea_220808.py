T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    # 조망권 찾기
    for i in range(2, N-2):
        h = 0
        for j in range(i-2, i+3):
            if j == i:
                continue
            else:
                if h < arr[j]:
                    h = arr[j]
        # print(h)
        if arr[i] > h:
            cnt += arr[i] - h
    print(f'#{tc} {cnt}')