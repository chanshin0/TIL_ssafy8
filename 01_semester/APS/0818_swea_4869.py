# [기본] 4일차 - 종이붙이기 (제출용)
def wtf_fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return wtf_fibo(n-1) + wtf_fibo(n-2)*2
    # n=3 일떄 왼쪽이 세로 기둥인 경우 n-1, 네모 기둥인 경우 n-2 네모는 갈라지니까 *2

T = int(input())
for tc in range(T):
    N = int(input())
    n = N//10

    print(f'#{tc+1} {wtf_fibo(n)}')

