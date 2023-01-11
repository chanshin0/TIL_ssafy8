# 이웃 원소의 합
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    s = [list(map(int, input().split())) for i in range(N)]
    # [[72, 76, 80], [16, 66, 37], [92, 53, 7]]


    max_sum = 0
    dx = [0, 0, 1, -1]
    dx= [1, -1, 0, 0]

    # 하드코딩;
    # for i in range(N):
    #     for j in range(N):
    #         if i == 0 and 0 < j < N-1: # 맨 위 행이면서 모서리 제외
    #             xb = s[i + 1][j]
    #             xl = s[i][j - 1]
    #             xr = s[i][j + 1]
    #             x_sum = xb+xl+xr
    #             if max_sum < x_sum:
    #                 max_sum = x_sum
    #
    #         elif i == N-1 and 0 < j < N-1: # 맨 아래 행이면서 모서리 제외
    #             xt = s[i - 1][j]
    #             xl = s[i][j - 1]
    #             xr = s[i][j + 1]
    #             x_sum = xt+xl+xr
    #             if max_sum < x_sum:
    #                 max_sum = x_sum
    #
    #         elif j == N-1 and 0 < i < N-1: # 맨 끝 열이면서 모서리 제외
    #             xt = s[i - 1][j]
    #             xb = s[i + 1][j]
    #             xl = s[i][j - 1]
    #             x_sum = xt+xl+xb
    #             if max_sum < x_sum:
    #                 max_sum = x_sum
    #
    #         elif j == 0 and 0 < i < N-1: # 맨 앞 열이면서 모서리 제외
    #             xt = s[i - 1][j]
    #             xb = s[i + 1][j]
    #             xr = s[i][j + 1]
    #             x_sum = xt+xb+xr
    #             if max_sum < x_sum:
    #                 max_sum = x_sum
    #
    #         elif 0 < i < N-1 and 0 < j < N-1: # 나머지 안엣줄 전부
    #             xt = s[i - 1][j]
    #             xb = s[i + 1][j]
    #             xr = s[i][j + 1]
    #             xl = s[i][j - 1]
    #             x_sum = xb+xt+xl+xr
    #             if max_sum < x_sum:
    #                 max_sum = x_sum
    print(f'#{tc} {max_sum}')
    # 218 291 316


