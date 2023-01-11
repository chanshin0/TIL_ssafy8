# 타일 로봇
T = int(input())
for tc in range(T):
    N = int(input()) # 명령 개수

    cnt = 0
    wall = [[0]*10 for _ in range(10)]                  # 10*10 벽
    for n in range(N):                                  # 명령 1개씩 for문
        yellow = list(map(int, input().split()))        # [2, 2, 4, 4] .....
        for i in range(10):
            for j in range(10):
                if i == yellow[0] and j == yellow[1]:   # 첫 꼭지점 만났을때
                    for di in range(yellow[2]-yellow[0]+1): # 0 1 2
                        for dj in range(yellow[3]-yellow[1]+1): # 0 1 2
                            if wall[i+di][j+dj] != 1:   # 1이 아니라면 1로 만들어라
                                wall[i+di][j+dj] = 1
                                cnt += 1
    print(f'#{tc+1} {cnt}')
