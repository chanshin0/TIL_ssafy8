T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = [list(map(int, input().split())) for i in range(N)]

    ismax = 0
    box = 0 # 사각형 넓이
    for i in range(N):
        for j in range(N):
            if s[i][j] == 1:
                box += 1
                if i < N-1 and j < N-1: # 아래-오른 테두리 아닐 떄
                    if s[i+1][j] == 0 and s[i][j+1] == 0: # 3바꾸다가 사각형의 맨 끝 지점에서,
                        if ismax < box: # 최대값 비교하고
                            ismax = box
                        box = 0 # box 초기화

                elif i == N-1: # 맨 아래 행일 때
                    if s[i][j+1] == 0 or j+1 > N-1: # 사각형의 맨 끝 지점에서
                        if ismax < box: # 최대값 비교하고
                            ismax = box
                        box = 0 # box 초기화

                elif j == N-1: # 맨 오른쪽 열일 때
                    if s[i+1][j] == 0 or i+1 > N-1: #사각형 맨 끝에서
                        if ismax < box: # 최대값 비교하고
                            ismax = box
                        box = 0 # box 초기화

    print(f'#{tc} {ismax}')
