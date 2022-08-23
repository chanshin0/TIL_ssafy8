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
            if stack == [] or icp[s[i]] > isp[stack[-1]]:       # 스택이 비었거나 토큰 우선순위가 더 클 때
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
                        break                                   # 스택이 비거나 우선순위 더 큰게 나오면 종료
                stack.append(s[i])                              # 토큰 스택에 push
        print(s2)
        print(stack)
    while stack:                                                # 남은 것 꺼내서 출력
        s2 += stack.pop()
    return s2

def cal (s):
    stack = []
    for i in range(len(s)):
        if s[i] not in icp:     # 숫자이면
            stack.append(s[i])
            print(stack, '#')
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
            print(stack)
    return stack[-1]

s = '(9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2)*4*7+4*3*8*2*6+(7*8*4*5)+3+7+(2+6+5+1+7+6+7*3*(6+2)+6+6)*2+4+2*2+4*9*3)'
s2 = postfix(d)
print(s2)
print(cal(s2))