def sum_of_digit(n):
    a = n%10
    b = n//10
    if n < 10:
        return a
    else:
        return a + sum_of_digit(b)

print(sum_of_digit(222))