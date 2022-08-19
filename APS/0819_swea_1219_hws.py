# [S/W 문제해결 기본] 4일차 - 길찾기
T = 10
for _ in range(T):
    tc, N = map(int, input().split())        # tc번호, 노드 총 개수
    arr = list(map(int, input().split()))
    # [0, 1, 0, 2, 1, 4, 1, 3, 4, 8, 4, 3, 2, 9, 2, 5, 5, 6, 5, 7, 7, 99, 7, 9, 9, 8, 9, 10, 6, 10, 3, 7]

    node = [[] for _ in range(100)]          # 총 정점이 100개이기 때문에 100개
    for i in range(len(arr)):
        if i % 2 == 0:                       # 인덱스가 짝수 일떄
            node[arr[i]].append(arr[i+1])    # 연결된 길을 인덱스 맞게 집어넣음
    # print(node)
    # [[1, 2], [4, 3], [9, 5], [7], [8, 3], [6, 7], [10], [99, 9], [], [8, 10], [], [], [], [], [], [], []]

    answer = 0
    stack = [0]                             # 출발은 0
    while len(stack) != 0:
        top = stack[-1]
        if top == 99:                       # 99(도착지)에 도달하면 종료
            answer = 1
            break

        if node[top] != []:                 # 연결된 길이 있으면(빈 리스트가 아니면)
            stack.append(node[top].pop())   # 이동
        else:
            stack.pop()                     # 연결된 길이 없으면 빽, 더이상 이동할 길이 없으면 0을 삭제하며 종료

    print(f'#{tc} {answer}')
