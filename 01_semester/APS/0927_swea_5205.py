# 퀵 정렬
def partition(l, r):
    pivot = A[l]
    i, j = l, r
    while i <= j:                           # 교차되면 종료
        while i <= j and A[i] <= pivot:         # 왼쪽에는 pivot보다 작으면 계속 +1
            i += 1
        while i <= j and A[j] >= pivot:         # 오른쪽에는 pivot보다 크면 계속 -1
            j -= 1
        if i < j:                               # i >= j이면 잘 모여있는 상태니까
            A[i], A[j] = A[j], A[i]             # 아니면 스왑
    A[l], A[j] = A[j], A[l]                     # 끝나면 피봇을 가운데 삽입
    return j                                    # 피봇위치 반환

def qsort(l, r):
    if l < r:
        s = partition(l, r)
        qsort(l, s-1)
        qsort(s+1, r)


T = int(input())
for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    qsort(0, N-1)
    print(f'#{tc+1} {A[N//2]}')