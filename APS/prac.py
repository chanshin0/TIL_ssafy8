def sudoku (arr):
    cnt = [0]*10 # 카운트 arr
    for i in range(9): # 1 2 3 4 ... 9
        cnt[arr[i]] += 1
    for i in range(1, 10):
        if cnt[i] != 1:
            return 0
    return 1


box = [[] for _ in range(9)]
print(list(range(0, 9, 3)))