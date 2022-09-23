def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:    # a[j]가 아직 사용되지 않았으면
                used[j] = 1
                p[i] = a[j]
                f(i+1, k)       # 다음 인덱스 정하러 보냄
                used[j] = 0     # 갔다가 돌아오면, a[j]를
                                # 다른 자리에서 쓸 수 있도록 해제






a = [1,2,3]
used = [0]*len(a)
p = [0]*len(a)
f(0, 3)