# [S/W 문제해결 기본] 6일차 - 계산기2
T = 10
for tc in range(T):
    N = int(input())
    s = input()
    op = ['+', '*']
    stack = []
    new_s = []
    for i in range(N):
        if s[i] not in op:          # 숫자일 때
            if s[i-1] != '*':
                new_s.append(int(s[i]))
        else:                       # 연산자일 때
             if s[i] == '+':
                 stack.append(s[i])
             else:                  # *일때
                 new_s.append(new_s.pop()*int(s[i+1]))

    while stack != []:              # 남아있는 + 꺼내서 계산
        a = new_s.pop()
        b = new_s.pop()
        stack.pop()
        new_s.append(b+a)

    print(f'#{tc+1} {new_s[0]}')

    # [22*]
    # [(+]
