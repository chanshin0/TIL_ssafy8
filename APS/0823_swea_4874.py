# [기본] 5일차 - Forth (제출용)
T = int(input())
for tc in range(T):
    s = list(input().split())
    # print(s)
    op = ['+', '-', '*', '/']
    cal = []
    for i in range(len(s)):
        if s[i] not in op:                          # 숫자일 떄(연산자 아닐때)
            if s[i] == '.':                             # 마지막까지 순회했을 때
                if len(cal) != 1:                        # 연산 안되고 남은 숫자가 있다면 에러
                    print(f'#{tc + 1} error')
                    break
                else:                                   # 모두 연산되어 하나만 남아 있다면 출력
                    print(f'#{tc + 1} {cal[-1]}')
            else:
                cal.append(s[i])
        else:                                       # 연산자일 때
            if len(cal) >= 2:                           # 스택에서 숫자꺼내서 연산하고 다시 집어넣음
                a = int(cal.pop())
                b = int(cal.pop())
                if s[i] == '+':
                    cal.append(b+a)
                elif s[i] == '-':
                    cal.append(b-a)
                elif s[i] == '*':
                    cal.append(b*a)
                elif s[i] == '/':
                    if a == 0:
                        print(f'#{tc + 1} error')
                        break
                    else:
                        cal.append(b//a)
            else:                                       # 연산자 꺼냈는데 연산할 숫자가 부족하다면 에러
                print(f'#{tc + 1} error')
                break

                # 10 2 + 3 4 + * 5 .
