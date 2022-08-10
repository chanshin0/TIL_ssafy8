T = int(input())
for tc in range(T):
    N = int(input())
    seq_lst = list(map(int, input()))
    # 찾아야할 지점 : 1이 나오는 지점
    cnt = 1 # 1을 셀때 기본값은 1
    max_cnt = 0 # 연속된 1의 개수의 최댓값
    for i in range(len(seq_lst)-1): # 0 ~ 8
        if seq_lst[i] == 1:  # 1다음에 경우의수는 0,1 두가지
            if seq_lst[i+1] == 1:
            # 1이 나오고, 그다음 요소도 1이라면
                cnt += 1
            # 연속한 1의개수 +1
            if seq_lst[i+1] == 0  or i == len(seq_lst)-2:
                # 연속이 끝나는 조건 : 다음이 0이거나 i가 마지막에서 2번째일때 
                # max_cnt 업데이트하고 cnt 초기화
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 1
            
    print(f'#{tc+1} {max_cnt}')

