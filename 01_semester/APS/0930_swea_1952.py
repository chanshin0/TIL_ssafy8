# 수영장
T = int(input())
for tc in range(T):
    fee = list(map(int, input().split()))
    month = list(map(int, input().split()))
    l = 0
    for i in month:
        if not i:
            l += 1

    y = 1
    m3 = l//2 + 1
    m = l
    d =
