# 부분 집합 가지치기 x
def f(i, N, s, t):
    global answer
    if i == N:        # 모든 원소가 고려된 경우
        return
    else:
        f(i+1, N, s+A[i], t)    # A[i]가 포함된 경우
        f(i+1, N, s, t)         # A[i]가 포함되지 않은 경우


A = [1,2,3,4,5,6,7,8,9]
bit = [0]*10
answer = 0
f(0, 10, 0, 10)
print(answer)