# 베이비진 판별

def babygin (s, k):
    tripet = 0
    run = 0
    s_lst = list(map(int, str(s)))
    # print(s_lst) [6, 6, 7, 7, 6, 7]
    cnt = [0]*(k+1)

    for i in range(len(s_lst)):
        cnt[s_lst[i]] += 1
    # print(cnt) [0, 0, 0, 0, 0, 0, 3, 3]
    i = 0
    while i < len(cnt):
        if cnt[i] >= 3:     # 카운트가 3보다 크면 트리펫 1, 카운트 3빼기
            tripet += 1
            cnt[i] -= 3
            continue
        if cnt[i-1] >= 1 and cnt[i] >= 1 and cnt[i+1] >= 1:
            run += 1
            cnt[i - 1] -= 1
            cnt[i] -= 1
            cnt[i + 1] -= 1
            continue
        i += 1

    if tripet + run == 2:
        return True
    else:
        return False

print(babygin(123532, 7))
