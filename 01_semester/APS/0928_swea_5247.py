# 연산
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    front = rear = -1
    que = [0] * 10000000
    rear += 1
    que[rear] = N  # enqueue
    visited[N] = 1
    while visited[M] == 0 and que:
        front += 1
        s = que[front]  # dequeue
        for i in [s + 1, s - 1, s * 2, s - 10]:
            if 0 < i <= 1000000 and visited[i] == 0:
                visited[i] = visited[s] + 1
                rear += 1
                que[rear] = i

    print(f'#{tc+1} {visited[M] - 1}')