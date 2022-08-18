# 당근 수확
T = int(input())
for tc in range(T):
    N = int(input()) # 5
    arr = list(map(int, input().split()))

    ismin = 0            # 차이가 최소인지 계산
    last_area = 0
    for i in range(N-1): # 0 1 2 3
        scv1 = 0
        scv2 = 0
        for j in arr[:i+1]:   # 일꾼1의 수확량이 arr[:i+1]까지의 합이면,
            scv1 += j

        for k in arr[i+1:N+1]:  # 일꾼2의 수확량은 arr[i+1:]의 합
            scv2 += k

        diff = abs(scv1-scv2)
        if i == 0:              # 비교를 위해 최소값에 일단 하나 집어넣음
            ismin = diff
        if diff <= ismin:
            ismin = diff
            last_area = i+1     # 최소값이 될때 마지막 영역의 인덱스는 i+1

    print(f'#{tc+1} {last_area} {ismin}')
