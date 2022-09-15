# 숫자판 점프
arr = [list(map(int, input().split())) for _ in range(5)]
mydigit = [[]for _ in range(6)]



temp = ''
for i in range(5):
    for j in range(5):
        mydigit[0].append(arr[i][j])

        delta = []
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < 5 and 0 <= nj < 5:
                delta.append(arr[ni][nj])
        set_delta = set(delta)
        print(delta)
        print(set_delta)
# 여섯번 델타이동한 경우의 수
