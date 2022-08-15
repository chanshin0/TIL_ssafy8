
while True:
    n = int(input())
    if n == 0:
        break
    # S 어레이
    while True:
        k = 1
        for i in range(1, n+1):
            k = k*i
            if k >= n:
                break
        break
    # S 어레이
    s = [1]       
    while True:
        if len(s) == k:
            break
        s.append(s[-1]*3)
    
    result = []
    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(s[j])
        result.append(subset)
        if len(result) == n:
            break

    print(result[n-1])