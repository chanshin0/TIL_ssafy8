# 이진수 제출용
T = int(input())
for tc in range(T):
    N, digit = input().split()

    digit_10 = int(digit, 16)

    ans = ''
    for j in range(int(N)*4-1, -1, -1):    # 15번 비트부터 0번 비트까지 (16개)
        if digit_10 & (1 << j):            # 1이면
            ans += '1'                     # 1
        else:                              # 0이면
            ans += '0'                     # 0
    print(f'#{tc+1} {ans}')
