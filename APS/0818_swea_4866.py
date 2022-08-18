# [기본] 4일차 - 괄호검사
T = int(input())
for tc in range(T):
    s = input()
    stack = []
    l_lst = ['{', '(']
    r_lst = ['}', ')']
    chk_lst = ['()', '{}']

    answer = 1
    for i in range(len(s)):
        if s[i] in l_lst:                     # 왼쪽 괄호 튀나오면 스택에 삽입
            stack.append(s[i])
            # print(stack, 1)
        elif s[i] in r_lst:                   # 오른쪽 괄호 체크
            if len(stack) == 0:
                answer = 0
                break
            elif stack.pop()+s[i] in chk_lst:   # 짝이 맞는지 체크하고 top삭제
                continue
            else:                             # 짝이 안맞으면 break
                answer = 0
                break

    if len(stack) != 0:                       # 다 돌렸는데도 stack이 남아있으면 0
        answer = 0
    print(f'#{tc+1} {answer}')



