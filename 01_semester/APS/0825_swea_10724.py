# 5099. [기본] 6일차 - 피자 굽기 (제출용)
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    chiz = list(map(int, input().split()))
    # [7, 2, 6, 5, 3]
    queue = list(range(1, M+1)) # 1 2 3 4 5

    # 화덕 돌리기
    front = queue[0]
    while True:
        queue.append(queue.pop(0))
        if queue[0] == front:
            for i in range(M):
                chiz[i] //= 2
                if chiz[i] == 0:
                    queue.pop(i)
        print(chiz)
        print(queue)
        if len(queue) == 1:
            break
    # [1, 2, 3, 4, 5]
    # [3, 1, 3, 2, 1]

