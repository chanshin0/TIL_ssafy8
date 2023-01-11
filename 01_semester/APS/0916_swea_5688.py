# 세제곱근을 찾아라
def binary(s,e):
    while s <= e:
        mid = (s+e)//2
        if mid**3 < N:
            s = mid+1
        elif mid**3 == N:
            return mid
        else:
            e = mid-1
    return -1

T = int(input())
for tc in range(T):
    N = int(input())

    print(f'#{tc+1} {binary(1, N)}')
