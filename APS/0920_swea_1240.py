# [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    code = [list(input()) for _ in range(N)]

    dict = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

    ans = ''
    for i in range(N):
        for j in range(0, M-7+1):
            check = code[i][j:j+7]
            check = ''.join(check)
            if check in dict:
                ### 여기서 len 8될떄까지 while문
                print(check)
                ans += str(dict.get(check))
                if len(ans) == 8:
                    break
        if len(ans) == 8:
            break

    print(ans)
    ans = '0'+ans
    temp = 0
    for i in range(1,9):
        if i%2:
            temp += int(ans[i])*3
        else:
            temp += int(ans[i])
        print(temp)
    if not temp%10:
        print(f'#{tc+1} {sum(map(int, ans))}')
    else:
        print(f'#{tc+1} 0')