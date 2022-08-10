T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = 10
    answer = 0
    for i in range(1, 1<<N):
        s = 0
        for j in range(N):
            if i & (1<<j): # j번 비트가 1이면 arr[j]가 부분집합에 포함
                s += arr[j]
        if s == 0:
            answer = 1
            break
    print(f'#{tc} {answer}')