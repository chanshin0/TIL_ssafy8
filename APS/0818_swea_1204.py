# [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T = 10
for tc in range(T):
    tc = int(input())
    arr = [list(map(int, input().split()))]

    for i in range(1000-1):
        for j in range(i, 1000-1):
            if arr[j]