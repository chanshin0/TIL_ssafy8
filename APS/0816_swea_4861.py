# [기본] 3일차 - 회문 (제출용)
def sleepy (arr):
    M = len(arr)//2
    if len(arr) % 2 == 0:
        if arr[M-1::-1] == arr[M:]:
            return True
    else:
        if arr[M-1::-1] == arr[M+1:]:
            return True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 가로찾기
    for i in range(N):
        for j in range(N-M+1): # 0
            str1 = arr[i][j:j+M]
            if sleepy(str1) == True:
                print(f'#{tc} {str1}')
                break
    # 세로찾기
    for k in range(N - M + 1):  # 0
        for i in range(N):
            str2 = ''
            for j in range(M):
                str2 += arr[j+k][i]

            if sleepy(str2) == True:
                print(f'#{tc} {str2}')
                break
