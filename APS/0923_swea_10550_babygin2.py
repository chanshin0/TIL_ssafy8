# Baby-gin
T = int(input())
for tc in range(T):
    num = int(input())
    cnt = [0]*12    # indexerror 방지

    i = 0
    while i < 6:
        cnt[num%10] += 1
        num //= 10
        i += 1

    tri = 0
    runn = 0
    i = 1
    while i < 10:
        if cnt[i] >= 3:
            cnt[i] -= 3
            tri += 1
            continue
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            runn += 1
            continue
        i += 1

    if runn + tri == 2:
        print(f'#{tc+1} Baby Gin')
    else:
        print(f'#{tc+1} Lose')