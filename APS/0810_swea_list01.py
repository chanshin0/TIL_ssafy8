T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0 # 총합 담을 변수
    # 모든 원소에 대해서 를 의미한다.
    for i in range(N):
        for j in range(N):
            # |arr[i][j] - 이웃한 원소|의 합 
            # 이웃 원소의 인덱스 ni, nj
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni, nj = i + di, j +dj # i,j의 이웃 원소의 인덱스 ni,nj
                if 0 <= ni < N and 0 <= nj < N:
                    answer += arr[i][j]-arr[ni][nj]
                    if answer < 0:
                        answer *= -1
    print(f'#{tc} {answer}')

