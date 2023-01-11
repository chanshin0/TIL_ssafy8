
T = int(input())
for tc in range(T):
    N = int(input()) # n의 크기
    n = list(map(int, input().split())) # 1 2 3 4 5 6 7 8 9 10

    for i in range(N-1): # 0 1 2 3 4 5 6 7 8
        min_idx = max_idx = i
        if i % 2 == 0: #  짝수번째 idx면
            for j in range(i+1, N): # 1 2 3 4 5 6 7 8 9
                if n[j] > n[max_idx]:
                    max_idx = j
            n[i], n[max_idx] = n[max_idx], n[i] 
            # 지금 꺼낸 ni랑 나머지 idx 돌면서 젤 큰 숫자랑 위치바꿈
        
        else: #  홀수번째 idx면
            for j in range(i+1, N): # 1 2 3 4 5 6 7 8 9
                if n[j] < n[min_idx]:
                    min_idx = j
            n[i], n[min_idx] = n[min_idx], n[i] 
            # 지금 꺼낸 ni랑 나머지 idx 돌면서 젤 작은거랑 위치바꿈

    rst = ' '.join(map(str, n[:10])) # 10개 컷
    print(f'#{tc+1} {rst}')