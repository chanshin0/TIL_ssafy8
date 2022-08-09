T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input()))
    cnt =  [0]*10 # 카드의 숫자는 0~9까지니까 10개
    for j in arr:
        cnt[j] += 1
    # cnt = [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]
    for idx, j in list(enumerate(cnt))[::-1]:
        if max(cnt) == j:
            print(f'#{tc+1} {idx} {j}')
            break