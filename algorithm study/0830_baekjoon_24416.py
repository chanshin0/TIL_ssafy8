# 알고리즘 수업 - 피보나치 수 1
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(5))