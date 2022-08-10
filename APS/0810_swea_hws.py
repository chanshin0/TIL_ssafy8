T = 10
for tc in range(T):
    N = 100
    s = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 1. 행의 합
    ismax = 0
    sum_diagonal = 0 # 얘는 다돌아야하니까
    sum_r_diagonal = 0
    for i in range(N): # 0 ~ 99
        sum_row = 0
        sum_col = 0
        for j in range(N):
            sum_row += arr[i][j]
    # 2. 열의 합
            sum_col += arr[j][i]
    # 3. \합
            if i == j: # i랑 j랑 일치하면 대각선
                sum_diagonal += arr[i][j]
    # 4. /합
            if i + j == 99: # 배열 크기-1이면 반대 대각선
                sum_r_diagonal += arr[i][j]
        if sum_row > ismax:
            ismax = sum_row
        if sum_col > ismax:
            ismax = sum_col

    if sum_diagonal > ismax:
        ismax = sum_diagonal
        # 대각선 합이 최대값인가?
    if sum_r_diagonal > ismax:
        ismax = sum_r_diagonal
    
    print(f'#{tc+1} {ismax}')

