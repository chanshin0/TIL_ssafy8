# [기본] 4일차 - 반복문자 지우기 (제출용)
T = int(input())
for tc in range(T):
    s = input()

    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
        # print(stack)
    print(f'#{tc+1} {len(stack)}')