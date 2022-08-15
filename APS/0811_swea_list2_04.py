# 달팽이
T = 2
for tc in range(T):
    s = int(input())
    # 123 123
    # 456 894
    # 789 765
    # for i in range(1, s+1):
    #  print(i, end=' ')
    #  print()
    s_lst = [i for i in range(1, s**2+1)]
    d = [[i+j for j in range(1, s+1)] for i in range(s)]
    for i in range(s-1)[::-1]: 2 1 0
        for j in range(s):
            if d[i][j] == d[i][-1]:
                pass
            d[i][j] += s*i


    # for i in range(4):
    #  for j in range(1, 4+1):
    #   print(i+j, end=' ')
    #  print()