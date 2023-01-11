# 컨테이너 운반
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    freights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    freights.sort()
    trucks.sort()

    ans = 0
    while trucks and freights:
        if freights[-1] <= trucks[-1]:
            ans += freights.pop()
            trucks.pop()
        else:
            freights.pop()

    print(f'#{tc+1} {ans}')
