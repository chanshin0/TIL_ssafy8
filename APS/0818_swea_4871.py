# [기본] 4일차 - 그래프 경로 (제출용)
T = int(input())
for tc in range(T):
    V, E = map(int, input().split()) # 노드 개수, 경로 개수
    arr = [input().split() for i in range(E)] # [['1', '4'], ['1', '3'], ['2', '3'], ['2', '5'], ['4', '6']]
    node = [[] for _ in range(V+1)] # [[], [], [], [], [], [], []] 0~6까지 7개인데 0뺴고
    print(arr)
    S, G = map(int, input().split()) # 출발과 도착
    stack = []

    for i in node:
        i.append()
    print(node)
