T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input()))
    cnt =  [0]*10 # 카드의 숫자는 0~9까지니까 10개
    for j in arr:
        cnt[j] += 1
    # cnt = [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]
    for idx, j in list(enumerate(cnt))[::-1]:
        # 같은 값이면 큰 수가 나와야 하기 때문에 cnt를 맨뒤부터 돌아서
        if max(cnt) == j: #cnt의 최댓값이 나올떄
            print(f'#{tc+1} {idx} {j}') # 출력하고 break
            break