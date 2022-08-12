# 최대 최소의 간격
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = list(map(int, input().split()))

    maxI = 0
    minI = 0
    for i in range(N): # 0 1 2 3 4 ...
        if s[i] == min(s):
            minI = i # 0
            break

    for j in range(N)[::-1]: # 4 3 2
        if s[j] == max(s):
            maxI = j # 4
            break

    # 만약 둘의 차가 음수면 -1 곱해라
    print(f'#{tc} {abs(maxI-minI)}')