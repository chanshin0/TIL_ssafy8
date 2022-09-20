# [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
T = in
for tc in range(T):
    N, M = map(int, input().split())
    code = [list(map(int, input())) for _ in range(N)]

    print(code)