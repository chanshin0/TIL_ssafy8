# 요리사
T = int(input())
for tc in range(T):
    N = int(input())
    ajdM = [list(map(int, input().split())) for _ in range(N)]
    foods = list(range(N))

    sub_foods = []
    for i in range(1<<N):
        temp = []
        for j in range(N): # 0 ~ N번째 비트까지
            if i & (1<<j):
                temp.append(foods[j])
        if len(temp) == N//2:
            sub_foods.append(temp)

