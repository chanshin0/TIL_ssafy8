# 이진탐색
def bi_search(k, l, r, cnt_l, cnt_r):
    global cnt
    if r < l:                           # 기본종료조건
        return
    if abs(cnt_r-cnt_l) > 1:            # 종료조건 1.
        return                          # 양 쪽 번갈아가며 선택하지 않으면 종료

    m = (l+r)//2
    if A[m] == k:                       # 종료조건 2.
        cnt += 1                        # 찾는 k가 m에 올 경우
        return
    elif A[m] > k:          # 왼쪽 선택
        r = m-1
        bi_search(k, l, r, cnt_l+1, 0)  # 왼쪽 탐색할때 오른쪽 카운트 초기화
    else:                   # 오른쪽 선택
        l = m+1
        bi_search(k, l, r, 0, cnt_r+1)  # 오른쪽 탐색할때 왼쪽 카운트 초기화

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(M):
        bi_search(B[i], 0, N-1, 0, 0)
    print(f'#{tc+1} {cnt}')