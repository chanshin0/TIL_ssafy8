# 당근밭 옆 고구마밭
T = int(input())
for tc in range(T):
    N = int(input())
    goguma = list(map(int, input().split()))

    julgis = [[] for _ in range(N)]
    j = 0 # 4
    for i in range(N):
        if i != 0 and i <= j:
            pass
        else:
            j = i
            julgis[i].append(goguma[j])
            while j <= N - 1:
                if j < N - 1 and goguma[j] < goguma[j + 1]:
                    julgis[i].append(goguma[j + 1])
                    j += 1
                else:
                    break
    ismax = 0
    for i in julgis:
        if len(i) >= ismax:
            ismax = len(i)

    cnt = 0
    big_julgi = []
    for i in julgis:
        if len(i) == ismax:
            big_julgi.append(sum(i))
        if i and len(i) > 1:
            cnt += 1

    a = max(big_julgi)
    if cnt == 0:
        a = 0

    print(f'#{tc+1} {cnt} {a}')