# [S/W 문제해결 기본] 3일차 - 회문2
def sleepy (arr):
    M = len(arr)//2
    if len(arr) % 2 == 0:
        if arr[M-1::-1] == arr[M:]:
            return True
    else:
        if arr[M-1::-1] == arr[M+1:]:
            return True

T = 10 # 10
for tc in range(T):
    arr= [input() for _ in range(100)]
    N = 100
    ismax = 0
    # 100개부터 줄여간다?
    # for k in range(N):
    #     M = 100
    #     for i in range(N):
    #         for j in range(N - M + 1):  # 0
    #             str1 = arr[k][j:j + M]
    #             if sleepy(str1) == True:
    #                 if len(str1) > ismax:
    #                     ismax = len(str1)
    #                     break
    #         M -= 1

    M = 100
    for k in range(N - M + 1):  # 1 2 3 4 ~  # 0
        for i in range(N): # 0 1 2 ~ 99
            str2 = ''
            for j in range(M): # 세로 str2 만드는 부분
                str2 += arr[j+k][k]
                # M =99, j - 0 1 2... k - 0 1 i - 0 1 2 ...
            if sleepy(str2) == True:
                if len(str2) > ismax:
                    ismax = len(str2)
                    break
    M -= 1

    print('#', ismax)
    # 세로 고치기.
