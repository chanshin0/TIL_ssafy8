# 배열 안에 t가 있으면 1, 아니면 0 출력
def f (i, N, t):
    if i == N:
        return 0        # 배열에 t가 없는 경우
    elif A[i] == t:
        return 1
    else:
        return f(i+1, N, t)

A = [1, 2, 3]
t = 2
answer = 1
f(0, 3)