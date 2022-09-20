N = float(0.625)

temp = ''
for i in range(1, 4,):
    print(i)
    if N & (1 >> i):
        temp += '1'
    else:
        temp += '0'