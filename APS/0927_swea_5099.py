# 피자 굽기
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    iscooking = pizza[:N]
    front = 0
    while len(iscooking) != 1:
        iscooking[front] //= 2
        if iscooking[front] == 0:
            iscooking.pop(front)
            if N < M:
                iscooking.append(pizza[N])
                N += 1
        else:
            front = (front+1)%N

    print(f'#{tc+1} {iscooking}')