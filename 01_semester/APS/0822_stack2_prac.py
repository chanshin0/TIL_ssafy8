infix = '3+4+5*6+7'
postfix = ''

op = ['+', '-', '*', '/'] # operator

stack = [0]*10
top = -1

for x in infix:
    if x not in op: # if '0' <= x <= '9'
        postfix += x
    else:
        top += 1        # push
        stack[top] = x

while top > -1:
    postfix += stack[top]   # pop
    top -= 1

print(postfix) # 2345/*+

# 숫자들을 먼저 쭉 집어넣고, 연산자는 스택에 담아 위에서부터 하나씩 꺼내서 뒤에 붙인다.
