# [기본] 3일차 - 회문 (제출용)
def sleepy (arr):
    M = len(arr)//2
    if arr[M-1::-1] == arr[M:]:
        return True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(N, M)
    print(arr)
    answer = []
    for i in range(N):
        for j in range(N-M+1): # 0 1 2
            str1 = arr[i][j:j+M]
            if sleepy(str1) == True:
                print(str1)



