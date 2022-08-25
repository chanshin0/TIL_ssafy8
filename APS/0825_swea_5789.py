# 현주의 상자 바꾸기
T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    box = [0]*N

    for q in range(Q): # 0 1
        L, R = map(int, input().split()) # 1 3 / 2 4
        for i in range(L, R+1):
            box[i-1] = q+1
    print(f'#{tc+1}', end=' ')
    print(*box)