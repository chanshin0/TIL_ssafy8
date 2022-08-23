# 계산기3
# 우선순위
icp = {'(' : 3, '+' : 1, '-' : 1, '*' : 2, '/' : 2, ')': -1}
isp = {'(' : 0, '+' : 1, '-' : 1, '*' : 2, '/' : 2, ')': -1}

def postfix (s):
    stack = []
    s2 = ''
    n = len(s)
    for i in range(n):
        if s[i] not in icp:                                 # 숫자일 때
            s2 += s[i]
        else:                                               # 연산자일 때
            if stack == [] or icp[s[i]] > isp[stack[-1]]:       # 스택이 비었거나 icp가 isp보다 크다면
                stack.append(s[i])                              # push
                # print(stack)
            elif s[i] == ')':                               # 닫는 괄호가 나오면 반복문 시작
                while True:
                    s2 += stack.pop()                           # top꺼내서 출력하고
                    if stack[-1] == '(':                        # 여는 괄호나오면 삭제하고 종료
                        stack.pop()
                        break
            else:
                while True:                                 # 꺼낸 토큰의 우선순위가 더 낮을 때
                    s2 += stack.pop()                           # top꺼내서 출력하고
                    if len(stack) == 0 or icp[s[i]] > isp[stack[-1]]:
                        break                                   # 스택이 비거나 isp가 icp보다 작은게 나올떄까지
                stack.append(s[i])                              # 토큰 스택에 push
    while stack:                                            # 남은 것 꺼내서 출력
        s2 += stack.pop()
    return s2

def cal (s):
    stack = []
    for i in range(len(s)):
        if s[i] not in icp:     # 숫자이면
            stack.append(s[i])
        else:                   # 연산자 나오면
            a = int(stack.pop())
            b = int(stack.pop())
            if s[i] == '+':
                stack.append(b+a)
            elif s[i] == '-':
                stack.append(b-a)
            elif s[i] == '*':
                stack.append(b*a)
            elif s[i] == '/':
                stack.append(b/a)
    return stack[-1]

T = 10
for tc in range(T):
    N = int(input())
    s = input()
    s2 = postfix(s)
    ans = cal(s2)
    print(f'#{tc+1} {ans}')