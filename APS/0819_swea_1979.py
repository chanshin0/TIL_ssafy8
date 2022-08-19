# 어디에 단어가 들어갈 수 있을까
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # [[0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]
    rev_arr = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rev_arr[i].append(arr[j][i])
    # [[0, 1, 0, 0, 1], [0, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 0], [1, 0, 0, 1, 1]]

    answer = 0
    for i in range(N):
        row_sum = 0                 # 가로행 여기서 초기화
        for j in range(N): # 0 1 2 3 4
            if arr[i][j] == 1:      # 가로행 체크
                row_sum += 1

            if arr[i][j] == 0 or j == N-1:  # 1 끊길 때 계산
                if row_sum == K:
                    answer += 1
                row_sum = 0

    for i in range(N):
        col_sum = 0
        for j in range(N):
            if rev_arr[i][j] == 1:      # 가로행 체크
                col_sum += 1

            if rev_arr[i][j] == 0 or j == N-1:  # 1 끊길 때 계산
                if col_sum == K:
                    answer += 1
                col_sum = 0

    print(f'#{tc+1} {answer}')

