
while True:
    n = int(input())
    if n == 0:
        break
    # S 어레이
    s = [1]
    while True:
        if len(s) == n:
            break
        s.append(s[-1]*3)
    print(s)