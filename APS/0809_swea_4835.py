T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    s = list(map(int, input().split()))
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    maxV = minV = 0 
    for i in range(M-1, N): # 슬라이싱
        prefix_sum = sum(s[i-(M-1):i+1]) # 구간합을 s[M-1]부터 계산
        if prefix_sum >= maxV:
            maxV = prefix_sum
        if prefix_sum <= minV or minV == 0:
            minV = prefix_sum
    print(f'#{tc+1} {maxV-minV}')
