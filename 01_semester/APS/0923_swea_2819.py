# 격자판의 숫자 이어 붙이기
# import sys
# sys.setrecursionlimit(10**5)

def dfs(i, j, char):
    char += arr[i][j]
    if len(char) == 7:
        if char not in ans:
            ans.append(char)
            return

    for di, dj in delta:
        ni = i+di
        nj = j+dj
        if 0 <= ni < 4 and 0 <= nj < 4 and len(char) < 7:
            dfs(ni, nj, char)


    return

T = int(input())
for tc in range(T):
    arr = [list(input().split()) for _ in range(4)]

    ans = []
    delta = [[0,1],[1,0],[0,-1],[-1,0]]
    for i in range(4):
        for j in range(4):
            mynum = ''
            dfs(i, j, mynum)
    print(ans)
    print(f'#{tc+1} {len(ans)}')