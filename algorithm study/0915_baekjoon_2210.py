# 숫자판 점프
def dfs(i, j):
    global temp
    ni = i+0
    nj = j+1
    if 0 <= ni < 5 and 0 <= nj < 5 and len(temp) < 6:
        temp += str(arr[ni][nj])
        dfs(ni, nj)

    ni = i + 1
    nj = j + 0
    if 0 <= ni < 5 and 0 <= nj < 5 and len(temp) < 6:
        temp += str(arr[ni][nj])
        dfs(ni, nj)

    ni = i + 0
    nj = j + -1
    if 0 <= ni < 5 and 0 <= nj < 5 and len(temp) < 6:
        temp += str(arr[ni][nj])
        dfs(ni, nj)

    ni = i + -1
    nj = j + 0
    if 0 <= ni < 5 and 0 <= nj < 5 and len(temp) < 6:
        temp += str(arr[ni][nj])
        dfs(ni, nj)

    if len(temp) == 6:
        if temp not in mydigit:
            mydigit.append(temp)
            temp = str(arr[i][j])
            dfs(ni,nj)

arr = [list(map(int, input().split())) for _ in range(5)]

mydigit = []
delta = [[0,1],[1,0],[0,-1],[-1,0]]
for i in range(5):
    for j in range(5):
        temp = str(arr[i][j])
        dfs(i, j)

print(mydigit)



