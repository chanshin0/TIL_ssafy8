# 간단한 소인수분해
T = int(input())
for tc in range(T):
    N = int(input())

    a, b, c, d, e = 0, 0, 0, 0, 0
    while True:
        if N % 2 != 0:
            break
        N = N / 2
        a += 1

    while True:
        if N % 3 != 0:
            break
        N = N / 3
        b += 1

    while True:
        if N % 5 != 0:
            break
        N = N / 5
        c += 1

    while True:
        if N % 7 != 0:
            break
        N = N / 7
        d += 1

    while True:
        if N % 11 != 0:
            break
        N = N / 11
        e += 1

    print(f'#{tc+1}', end=' ')
    print(a, b, c, d, e)
