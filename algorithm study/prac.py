def isdecimal(num):
    for l in range(1, int(num)+1, 2):
        if num % 2 == 0 or num == 1:
            return False
        elif num % l == 0 and l not in [1, num]:
            return False
    return True

n = int(input())
j_lst = []
answer = []
for i in range(n):
    s = int(input())
    for j in range(1, s+1, 2):
        if isdecimal(j):
            j_lst.append(j)

    for k in j_lst[:int(len(j_lst)/2)+1]:
        if isdecimal(s-k) == True:
            answer.append(sorted([k, s-k]))
    print(answer[-1][0], answer[-1][1])
