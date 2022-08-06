n = int(input())
num_lst=[]
for i in range(n):
    s = int(input())
    for j in range(1,s+1):
        if s % j == 0:
            num_lst.append()

# s/2가 소수라면, 그 두개를 출력.
# else: 
# range(s)에서 짝수거나 s의 약수를 제외한 것을 j라고 했을때
# s-j가 list_j 안에 있으면 그 두 개를 출력

# 1 2 4 8 16 / 3 5 7 9 11 13 15 /
# 1 2 5 10 / 3 7 
# 1 2 3 6