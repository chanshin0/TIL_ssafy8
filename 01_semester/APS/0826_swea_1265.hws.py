# [S/W 문제해결 응용] 9일차 - 달란트2
T = int(input())
for tc in range(T):
    N, P = map(int, input().split())

    a = N // P
    b = N % P
    talent = [a]*P
    for i in range(b):
        talent[i] += 1

    ans = 1
    for i in talent:
        ans *= i

    print(f'#{tc+1} {ans}')