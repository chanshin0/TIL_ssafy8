# 병합 정렬
# 인덱스 슬라이싱하지 않고 인덱스만 넘겨주는 방법

def msort(i, N):                    # 병합구간의 시작 인덱스, N구간의 원소 개수
    global cnt
    if N == 1:                      # 분할한 원소가 1개만 남은 경우
        return
    else:
        msort(i, N//2)              # 병합할 구간의 왼쪽 시작 인덱스
        msort(i+N//2, N-N//2)         # 병합할 구간의 오른쪽 시작 인덱스
        # 리턴값 없이 i, j=i+N//2 계산가능
        if arr[i+N//2-1] > arr[i+N-1]:   # 왼쪽구간의 마지막 원소와 오른쪽 구간의 마지막 원소 비교해서 왼쪽이 더 크면 cnt++
            cnt += 1                     # 문제에서 요구하는 두번째 출력
        k = 0
        l, r = i, i+N//2
        while l < i+N//2 and r < i+N:    # 왼쪽 구간, 오른쪽 구간 남아있으면
            if arr[l] <= arr[r]:         # 오름차순이면, 작은 숫자 먼저 temp에 복사
                temp[k] = arr[l]
                l += 1                   # 왼쪽구간에서 선택된 경우 i++
            else:
                temp[k] = arr[r]
                r += 1                   # 오른쪽구간에서 선택된 경우 j++
            k += 1
        while l < i+N//2:                # 왼쪽 구간에 남은 숫자가 있으면 모두 복사
            temp[k] = arr[l]
            l += 1
            k += 1
        while r < i+N:
            temp[k] = arr[r]
            r += 1
            k += 1
        for k in range(N):              # 병합한 결과를 원본에 복사
            arr[i+k] = temp[k]
        return i

T= int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    temp = [0]*N
    cnt = 0
    msort(0, N)

    print(f'#{tc+1} {arr[N//2]} {cnt}')
