# [모의 SW 역량테스트] 홈 방범 서비스

# k값에 따라 가능한 모든 델타를 반환하는 함수
# k=3이면, 0,1,2,-1,2중에서 두 개 뽑았을 때 각 절대값의 합이 k를 넘지않는 모든 경우의 수를 저장
def make_delta(k):
    delta = [[0, 0]]
    temp_lst = list(range(k)) + list(range(-1, -k, -1))  # 0 1 2 -1 -2
    for i in range(len(temp_lst)):
        for j in range(i, len(temp_lst)):
            if [temp_lst[i], temp_lst[j]] not in delta and abs(temp_lst[i]) + abs(temp_lst[j]) < k:
                delta.append([temp_lst[i], temp_lst[j]])
            if [temp_lst[j], temp_lst[i]] not in delta and abs(temp_lst[i]) + abs(temp_lst[j]) < k:
                delta.append([temp_lst[j], temp_lst[i]])
    return delta

# 모든 델타리스트를 인덱스에 맞춰 넣음
all_delta = [[]*(22) for _ in range(22)]
for i in range(1, 22):
    all_delta[i] = make_delta(i)

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    dosi = [list(map(int, input().split())) for _ in range(N)]

    compare = []
    for i in range(N):
        for j in range(N):
            for k in range(1, N+2):
                cost = -(k**2 + (k-1)**2)
                house = 0
                for di, dj in all_delta[k]:     # k=1부터 모든 델타 탐색
                    ni = i+di
                    nj = j+dj
                    if 0 <= ni < N and 0 <= nj < N and dosi[ni][nj] == 1:
                       house += 1
                       cost += M

                if cost >= 0:                   # 탐색 후 손해가 아니면
                    compare.append(house)       # 집 개수 저장

    print(f'#{tc+1} {max(compare)}')            # 그 중 최댓값 출력







