T = int(input()) # 전체 Testcase 개수
for tc in range(1, T+1): # testcase for문
    N = int(input()) # 상자 개수
    arr = list(map(int, input().split())) # 각 상자의 높이  
    maxV = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
            if maxV < cnt:
                maxV = cnt
    print(f'#{tc} {maxV}')