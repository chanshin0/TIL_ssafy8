T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = list(map(int, input().split()))
    # [3, 2, 1, 4, 5]

    ismax = s[0]+s[1] # 최대값
    ismin = s[0]+s[1] # 최소값 암거나 잡아놓고
    for i in range(N-1): # 0 1 2 3
        n_sum = s[i] + s[i+1] # 0~N-2까지 이웃 합 계산 01 12 23 34
        if ismax < n_sum:
            ismax = n_sum
            # print(ismax)
        if ismin > n_sum:
            ismin = n_sum
            # print(ismin)

    print(f'#{tc} {ismax} {ismin}')


