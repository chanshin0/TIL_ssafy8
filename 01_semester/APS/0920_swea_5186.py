# 이진수2
def bi_num(n):
    temp = ''
    a = 2**-1
    while n:                      # n이 0되면 종료
        temp += str(n//a)[:1]       # n을 a로 나눈 몫은 temp에 저장하고
        n %= a                      # 나머지는 n에 재할당
        a *= 2**-1
        if len(temp) > 12:
            return 'overflow'
    return temp

T = int(input())
for tc in range(T):
    N = float(input())

    print(f'#{tc+1} {bi_num(N)}')