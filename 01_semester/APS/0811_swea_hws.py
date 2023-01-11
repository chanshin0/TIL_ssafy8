T = 10
for tc in range(T):
    n = int(input()) #tc 번호
    arr = [list(map(int, input().split())) for _ in range(100)]

    xi = 0 #출발지점 열 99
    xj = 0 #출발지점 행 57
    for i in range(100): # 0 ~ 99
        for j in range(100): # 0 ~ 99
            if arr[i][j] == 2:
                 xi = i
                 xj = j
                 
    for k in range(xi)[::-1]: # 도착지 있는 열 탐색. 98 97 96 95 ..
        while arr[k][xj] != 0:
            if 0 < xj < 99:
                if arr[k][xj-1] == 1: # xj열의 왼쪽 탐색
                        xj -= 1
                elif arr[k][xj+1] == 1: # xj열의 오른쪽 탐색
                        xj += 1

            elif xj == 0:
                if arr[k][xj+1] == 1: # xj열의 오른쪽 탐색
                        xj += 1

            elif xj == 99:
                if arr[k][xj-1] == 1: # xj열의 왼쪽 탐색
                        xj -= 1
      
        if k == 0: # 도착지까지 오면 xj반환
            print(f'#{tc+1} {xj}')



        
