# [S/W 문제해결 기본] 6일차 - 계산기2
T = int(input())
for tc in range(T):
    N = int(input())
    s = input()
    op = ['+', '*']
    stack = [0]*len(s)
    top = -1
    for i in s:
        if i not in op: # 숫자일 때
            top += 1
            stack[top] = int(i)
    print(stack)