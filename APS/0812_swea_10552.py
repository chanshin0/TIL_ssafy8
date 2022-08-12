T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = list(map(int, input().split()))

    cnt = 0
    for j in range(N):
        for i in range(1, N):
            if s[i] < s[i-1]:
                s[i], s[i-1] = s[i-1], s[i]
                # 이렇게 하면 맨 끝에 젤 큰게 정렬됨.
                # 그래서 범위도 하나씩 줄여가면서 하면 된다.
                cnt += 1
    print(f'#{tc} {cnt}')