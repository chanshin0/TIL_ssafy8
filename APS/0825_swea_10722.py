# 5097. [기본] 6일차 - 회전 (제출용)
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))

    cnt = 0
    while True:
        if cnt == M:
            break
        front = seq.pop(0)
        seq.append(front)
        cnt += 1


    print(f'#{tc+1} {seq[0]}')