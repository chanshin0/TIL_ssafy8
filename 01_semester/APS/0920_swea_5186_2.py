# 이진수2
T = int(input())
for tc in range(T):
    N = float(input())
    n = len(N[2:])

    temp = ''
    for i in range(1, n+1):
        if int(N[2:]) & (1 >> i):
            temp += '1'
        else:
            temp += '0'
    print(temp)