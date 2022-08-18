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
    #100개부터 줄여간다?
    for k in range(N):
        M = 100
        for i in range(N):
            for j in range(N - M + 1):  # 0
                str1 = arr[k][j:j + M]
                if sleepy(str1) == True:
                    if len(str1) > ismax:
                        ismax = len(str1)
                        break
            M -= 1

    arr2 = []
    for i in range(N):
        for j in range(N):
            arr2.append(arr[j][i])
    print(arr2)

    for k in range(N):
        M = 100
        for i in range(N):
            for j in range(N - M + 1):  # 0
                str1 = arr2[k][j:j + M]
                if sleepy(str1) == True:
                    if len(str1) > ismax:
                        ismax = len(str1)
                        break
            M -= 1


    print('#', ismax)
    # 세로 고치기.
