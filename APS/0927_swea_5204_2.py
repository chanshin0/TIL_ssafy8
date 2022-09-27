# 병합정렬 다른 방법
def msort(A):
    global cnt
    N = len(A)
    if N == 1:                    # 원소가 하나남은 경우 분할 중지
        return A
    else:
        # N = r - l +1
        left = A[0:N//2]
        right = A[N//2:]
        if left[-1] > right[-1]:
            cnt += 1

        left = msort(left)
        right = msort(right)
        # A = []
        # while len(left) > 0 and len(right) > 0:     # 양쪽에 원소가 남아있으면
        #     if left[0] < right[0]:
        #         A.append(left.pop(0))
        #     else:
        #         A.append(right.pop(0))
        # if len(left) > 0:                           # 남은 원소가 있으면
        #     A += left
        # if len(right) > 0:
        #     A += right
        # return A
        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
        return A

T = int(input())
for tc in range(T):
    L = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = msort(arr)

    print(f'#{tc+1} {arr[L//2]} {cnt}')