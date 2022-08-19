# 파리 퇴치

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # [[1, 3, 3, 6, 7], [8, 13, 9, 12, 8], [4, 16, 11, 12, 6], [2, 4, 1, 23, 2], [9, 13, 4, 7, 3]]

    pentakill = 0
    for i in range(N-M+1): # 0 1 2 3
        for j in range(N-M+1):
            kill = 0                            # 여기서 초기화
            for mi in range(M): # 0 1
                for mj in range(M):
                    kill += arr[i+mi][j+mj]

            if kill > pentakill:                # 여기서 최대값 비교
                pentakill = kill
    print(f'#{tc+1} {pentakill}')
