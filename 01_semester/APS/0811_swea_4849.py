# 횟수 세는 함수
def check_cnt (P, A):
    c = int((1+P)/2)
    l = 1
    r = P
    cnt = 0
    while True:
        if A == c:
            break
        # 찾는 쪽이 중간보다 클 때와 작을 때로 구분
        elif A > c:
            l = c
            c = int((l+r)/2)
            cnt += 1
        elif A < c:
            r = c
            c = int((l+r)/2)
            cnt += 1
    return cnt

T = int(input())
for tc in range(T):
    P, A, B = map(int, input().split()) 

    if check_cnt(P, A) == check_cnt(P, B):
        print(f'#{tc+1} 0')
    elif check_cnt(P, A) > check_cnt(P, B):
        print(f'#{tc+1} B')
    elif check_cnt(P, A) < check_cnt(P, B):
        print(f'#{tc+1} A')
