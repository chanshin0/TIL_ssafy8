# Baby-gin
def f(i, k):
    if i == k:
        ru = 0
        tri = 0
        if card[0] == card[1] and card[1] == card[2]:
            tri += 1
        if card[0] + 1 == card[1] and card[1] + 1 == card[2]:
            ru += 1
        if card[3] == card[4] and card[4] == card[5]:
            tri += 1
        if card[3] + 1 == card[4] and card[4] + 1 == card[5]:
            ru += 1
        if tri + ru == 2:
            return 1
        else:
            return 0
    else:
        for j in range(i, k):  # 자리 바꿔서 순열 만들기
            card[i], card[j] = card[j], card[i]
            if f(i + 1, k):
                return 1
            card[i], card[j] = card[j], card[i]
        return 0


T = int(input())
for tc in range(1, T + 1):
    card = list(map(int, input()))
    ans = f(0, 6)
    if ans:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
