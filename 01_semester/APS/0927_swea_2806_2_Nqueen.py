# 다른 방법
def f(i, N):
    global cnt
    if i == N:
        cnt += 1
    else:
        for j in range(N):
            if col[j] == 0 and d1[i+j] == 0 and d2[i+N-1-j] == 0:
                col[j] = 1
                d1[i+j] = 1
                d2[i+N-1-j] = 1
                f(i+1, N)
                col[j] = 0
                d1[i + j] = 0
                d2[i + N - 1 - j] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    col = [0]*N
    d1 = [0]*(N+N+1)
    d2 = [0]*(N+N+1)
    cnt = 0
    f(0, N)

    print(f'#{tc+1} {cnt}')