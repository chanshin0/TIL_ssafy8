for i in range(1, 4):
    for j in range(1,4):
        if i != j:
            for k in range(1,4):
                if k not in [i, j]:
                    print(i, j, k)