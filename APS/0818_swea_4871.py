# [기본] 4일차 - 그래프 경로 (제출용)
T = int(input())
for tc in range(T):
    V, E = map(int, input().split()) # 노드 개수, 경로 개수
    arr = [list(map(int, input().split())) for i in range(E)]
    node = [[] for _ in range(V+1)] # [[], [], [], [], [], [], []] 0~6까지 7개인데 0뺴고
    # print(arr)
    S, G = map(int, input().split()) # 출발과 도착

    for i in arr:
        node[i[0]].append(i[1])   # 인덱스 번호에 맞게 연결된 노드 저장
    # print(node) -> [[], [4, 3], [3, 5], [], [6], [], []]

    stack = [S]
    answer = 0
    for _ in range(E+1):
        top = stack[-1]
        if top == G:            # 목적지 도착하면 종료
            answer = 1
            break

        if node[top] != []:                 # 빈리스트(연결된 곳이 없음) 아니면 이동
            stack.append(node[top].pop())
        else:
            stack.pop()                     # 빈리스트이면 빽
        # print(stack)

    print(f'#{tc+1} {answer}')