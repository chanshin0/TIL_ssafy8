T = int(input())
for tc in range(1,T+1):
    n = int(input())
    s = list(map(int, input().split()))
    maxV = 0
    for j in s:
        if j > maxV:
            maxV = j
    minV = 1000000
    for j in s:
        if j <= minV:
            minV = j
    print(f'#{tc} {maxV-minV}')