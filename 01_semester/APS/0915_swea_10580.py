# 전봇대
T = int(input())
for tc in range(T):
    N = int(input())
    left = []                   # 왼쪽 봇
    right = []                  # 오른쪽 봇
    for i in range(N):
        a, b = map(int, input().split())
        left.append(a)
        right.append(b)

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if left[i] < left[j]:           # 왼쪽이 높은데
                if right[i] > right[j]:     # 오른쪽은 낮으면
                    cnt += 1                # 교차
            else:
                if right[i] < right[j]:     # 왼쪽이 낮은데
                    cnt += 1                # 오른쪽은 높으면
    print(f'#{tc+1} {cnt}')                 # 교차