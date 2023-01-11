# 베이비진 게임
def babe(deck):
    i = 1
    while i < 10:
        if deck[i] >= 3:
            return 1
        if deck[i] >= 1 and deck[i+1] >= 1 and deck[i+2] >= 1:
            return 1
        i += 1
    return 0

T = int(input())
for tc in range(T):
    cards = [0]+list(map(int, input().split()))
    deck1 = [0]*12
    deck2 = [0]*12
    ans = 0
    for i in range(1, 13):
        if i%2:
            deck1[cards[i]] += 1
            if babe(deck1):
                ans = 1
                break
        else:
            deck2[cards[i]] += 1
            if babe(deck2):
                ans = 2
                break

    print(f'#{tc+1} {ans}')

