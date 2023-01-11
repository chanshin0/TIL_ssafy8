# 숫자 배열 회전
def rotate (arr):
    n = len(arr)
    r_arr = [[0]*n for _ in range(n)]
    for ri in range(n):
        for rj in range(1, n+1): # 1 2 3
            r_arr[ri][rj-1] = arr[n-rj][ri]
    return r_arr

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    rotate1 = rotate(arr) # 90
    rotate2 = rotate(rotate1) # 180
    rotate3 = rotate(rotate2) # 270
    # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    # [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

    print(f'#{tc+1}')
    for i in range(N): # 0 1 2
        print(''.join(map(str, rotate1[i])), end=' ')
        print(''.join(map(str, rotate2[i])), end=' ')
        print(''.join(map(str, rotate3[i])), end=' ')
        print()





