# 이진수 제출용
# 진수 변환 함수 사용
T = int(input())
for tc in range(T):
    N, digit = input().split()

    digit_10 = int(digit, 16)
    digit_2 = bin(digit_10)[2:]
    while len(digit)*4 != len(digit_2):
        digit_2 = '0' + str(digit_2)
    print(f'#{tc+1} {digit_2}')

