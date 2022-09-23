# Baby-gin
def f(i, k):
    if i == k:
        runn = 0
        tri = 0
        if num[0] == num[1] and num[1] == num[2]:
            tri += 1
        if num[3] + 1 == num[4] and num[4] + 1 == num[5]:
            runn += 1
        if runn + tri == 2:
            return 1
        return 0

    else:
        for j in range(i, k):
            num[i], num[j] = num[j], num[i]
            if f(i+1, k):   # 얘가 1을 반환하면
                return 1    # 1반환, 종료
            num[i], num[j] = num[j], num[i]
        return 0            # 1반환 안되고 여까지 내려왔으면 0

T = int(input())
for tc in range(T):
    num = list(map(int, input()))

    ans = f(0,6)  # 맨 처음 인덱스, num의 길이
    print(f'#{tc+1} Baby Gin') if ans else print(f'#{tc+1} Lose')