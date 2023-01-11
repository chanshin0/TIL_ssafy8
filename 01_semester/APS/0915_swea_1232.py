# 사칙연산
def postorder(n):
    if n:
        a = postorder(left[n])
        b = postorder(right[n])
        if tree[n] in operator:         # 노드 n의 값이 연산자일 때,
            if a == None or b == None:
                pass
            else:                            # a와 b값이 반환된다면
                if tree[n] == operator[0]:
                    tree[n] = (a+b)
                elif tree[n] == operator[1]:
                    tree[n] = (a-b)
                elif tree[n] == operator[2]:
                    tree[n] = (a*b)
                elif tree[n] == operator[3]:
                    tree[n] = (a//b)
            postorder(n // 2)                 # 연산 후, 값을 tree[n]에 덮어씌우고 재순회
        else:
            return tree[n]              # 노드 n의 값이 연산자 아니면 반환

T = 10
for tc in range(T):
    N = int(input())
    left = [0]*(N+1)
    right = [0]*(N+1)
    tree = [0]*(N+1)
    for n in range(N):
        a, b, *c = input().split()
        if len(c) == 2:                 # 노드값이 연산자일떄
            left[int(a)] = int(c[0])
            right[int(a)] = int(c[1])
            tree[int(a)] = b
        else:                           # 숫자일 때
            tree[int(a)] = int(b)

    operator = ['+', '-', '*', '/']
    postorder(1)

    print(f'#{tc+1} {tree[1]}')