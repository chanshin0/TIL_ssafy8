T = int(input())
for tc in range(1, T+1):
    n, N = input().split() #1 #2 ...
    N = int(N)

    weird = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    arr = input().split()

    answer = []
    for i in weird:
        for j in arr:
            if j == i: # arr 하나씩 꺼내서 순서대로 집어넣음
                answer.append(j)

    print(n, end='\n')
    print(' '.join(answer))

