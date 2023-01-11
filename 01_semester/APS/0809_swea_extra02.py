T = int(input())
for tc in range(T):
    N = int(input()) # 당근 개수
    c_arr = list(map(int, input().split())) # 당근 크기 arr
    # i < i+1 이면 cnt +1, i >= i+1이면 cnt 초기화
    cnt = 1 # 기본값 1
    max_cnt = 1 # 최댓값의 기본값도 1
    for i in range(N-1): # 0 1 2 3 
        if c_arr[i] < c_arr[i+1]:
            cnt += 1
            if cnt > max_cnt:
                # cnt의 최댓값을 m_cnt에 저장
                max_cnt = cnt
        else:
            cnt = 1
    print(f'#{tc+1} {max_cnt}')