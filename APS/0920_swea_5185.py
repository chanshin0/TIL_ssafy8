# 이진수 제출용
T = int(input())
for tc in range(T):
    N, digit = input().split()
    dict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

    ans = ''
    for i in digit:
        temp = ''
        if i.isdigit():                     # 숫자이면
            a = int(i)
            while a:
                temp = str(a%2) + temp          # 2로 나눈 나머지 거꾸로 읽기
                a //= 2
        else:                               # 알파벳이면
            a = dict[i]                         # 숫자로 바꿔서
            while a:                            # 2로 나눈 나머지 거꾸로 읽기
                temp = str(a%2) + temp
                a //= 2

        while len(temp) < 4:                # temp 4자리로 맞춰주기
            temp = '0' + temp

        ans += temp

    print(f'#{tc+1} {ans}')
