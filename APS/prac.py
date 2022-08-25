T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    s = [list(map(int, input().split())) for i in range(N)]

    ismax = 0
    box = 0  # 사각형 넓이
    for i in range(N):
        for j in range(N):
            if s[i][j] == 1:
                box += 1
                if s[i + 1][j] == 0 and s[i][j + 1] == 0:  # 사각형의 끝일 때,
                    if ismax < box:  # 최대값 비교하고
                        ismax = box
                    box = 0  # box 초기화
    print(f'#{tc} {ismax}')