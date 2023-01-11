# 스도쿠 검증
def sudoku (arr):
    cnt = [0]*10 # 카운트 arr
    for i in range(9): # 1 2 3 4 ... 9
        cnt[arr[i]] += 1
    for i in range(1, 10):
        if cnt[i] != 1:
            return 0
    return 1

T = int(input())
for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = 0
    for i in range(9):
        ans = sudoku(arr[i])        # 가로줄 검증
        if ans == 0:
            break
        col = [] # 세로줄 검증 arr
        for j in range(9):
            col.append(arr[j][i])
        ans = sudoku(col)           # 세로줄 검증
        if ans == 0:
            break

    box = [[] for _ in range(9)]
    i = 0
    for di in [0, 3, 6]:
        for dj in [0, 3, 6]:
            for bi in range(3): # 0 1 2
                for bj in range(3): # 0 1 2
                    box[i].append(arr[di+bi][dj+bj])
            i += 1
    # print(box)

    for i in range(9):
        if ans == 0:
            break
        ans = sudoku(box[i])

    print(f'#{tc+1} {ans}')
