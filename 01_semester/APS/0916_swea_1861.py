# 정사각형 방
def recur(i, j):            # 이동할 방 찾는 함수
    global cnt
    for di, dj in delta:
        ni = i+di
        nj = j+dj
        if 0 <= ni < N and 0 <= nj < N:
            if room[ni][nj] - room[i][j] == 1:  # 1차이나면
                cnt += 1                        # 카운트 하고
                recur(ni, nj)                   # 이동한 방에서 다시 리콜


T = int(input())
for tc in range(T):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]


    cnt_list = [[0]*N for _ in range(N)]
    delta = [[0,1],[1,0],[0,-1],[-1,0]]
    for i in range(N):
        for j in range(N):                  # 모든 방에서 함수 호출하고 cnt 기록
            cnt = 1
            recur(i, j)
            cnt_list[i][j] = cnt

    ismax = 0
    for i in range(N):
        for j in range(N):
            if cnt_list[i][j] > ismax:      # 이동한 방의 최대값 찾음
                ismax = cnt_list[i][j]

    ans_lst = []
    for i in range(N):
        for j in range(N):
            if cnt_list[i][j] == ismax:     # 최대값일때 몇번에서부터 시작했는지
                ans_lst.append(room[i][j])

    print(f'#{tc+1} {min(ans_lst)} {ismax}')    # 그중 가장 작은것 출력